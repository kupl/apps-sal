n, m = list(map(int, input().split()))
li = list(map(int, input().split()))
ans = 0
q = sorted(li, reverse=True)
for i in range(m):
    if q[i] * 4 * m >= sum(li):
        ans += 1
if ans == m:
    print("Yes")
else:
    print("No")
