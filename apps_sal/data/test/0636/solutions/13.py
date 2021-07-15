n,k = map(int, input().split())
l = list(map(int, input().split()))
q = [[1000000000,10000]]
ans = 0
s = ""
for i in range(n):
    q.append([l[i], i+1])
q = list(sorted(q))
while q[0][0] <= k:
    k -= q[0][0]
    ans += 1
    s += str(q[0][1])+" "
    q.pop(0)
print(ans)
print(s.strip())
