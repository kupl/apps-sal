N, K = map(int, input().split())
data = list(map(int, input().split()))
s = (N - K) // (K - 1)
a = (N - K) % (K - 1)
if a == 0:
    print(s + 1)
else:
    print(s + 2)
