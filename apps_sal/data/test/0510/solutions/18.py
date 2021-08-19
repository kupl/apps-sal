(a, b, c, d) = map(int, input().split())
ar = [a, b, c]
ar.sort()
left = max(0, d - abs(ar[1] - ar[0]))
right = max(0, d - abs(ar[2] - ar[1]))
print(left + right)
