N, K, M = map(int, input().split())
A = list(map(int, input().split()))

x = (M * N) - sum(A)
if x < 0:
    print("0")
elif x <= K:
    print(x)
else:
    print("-1")
