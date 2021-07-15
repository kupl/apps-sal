W, a, b = map(int, input().split())
L = [b - (a + W), a - (b + W), 0]
print(max(L))
