(a, b, c, d) = list(map(int, input().split()))
diff = a + b - (c + d)
if diff == 0:
    print('Balanced')
elif diff > 0:
    print('Left')
else:
    print('Right')
