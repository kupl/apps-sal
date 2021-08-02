N, K = map(int, input().split())
a = N % K

if a <= abs(a - K):
    print(a)
else:
    print(abs(a - K))
