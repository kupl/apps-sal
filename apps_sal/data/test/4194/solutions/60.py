(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
if sum(a[:m]) > n:
    print(-1)
else:
    print(n - sum(a[:m]))
