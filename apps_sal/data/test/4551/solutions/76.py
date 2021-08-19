(a, b, c, d) = map(int, input().split())
print('Left') if a + b > c + d else print('Right') if a + b < c + d else print('Balanced')
