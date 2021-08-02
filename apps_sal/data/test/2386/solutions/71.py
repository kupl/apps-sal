N = int(input())
A = sorted([int(x) - i for i, x in enumerate(input().split(), 1)])
mid = N // 2
ans = sum(list([abs(x - A[mid]) for x in A]))
if N % 2 == 0:
    _mid = N // 2 + 1
    _ans = sum(list([abs(x - A[_mid]) for x in A]))
    ans = min(ans, _ans)
print(ans)
