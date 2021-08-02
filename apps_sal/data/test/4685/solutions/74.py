a, b, c = map(int, input().split())
k = int(input())
print(max(a, b, c) * (2**k - 1) + a + b + c)
