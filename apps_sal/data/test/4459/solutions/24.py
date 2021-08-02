N = int(input())
A = list(map(int, input().split()))
d = dict()
for i in range(N):
    if d.get(A[i]) is None:
        d[A[i]] = 1
    else:
        d[A[i]] += 1
ans = 0
for key, value in list(d.items()):
    if key <= value:
        ans += value - key
    else:
        ans += value
print(ans)
