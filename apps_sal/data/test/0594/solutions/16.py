(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = max(max(A), min(A) * 2)
if min(B) > res:
    print(res)
else:
    print(-1)
