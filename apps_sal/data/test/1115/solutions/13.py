n = int(input())
a = list(map(int, input().split()))
m = int(input())
p = []
for i in range(m):
    l,r = map(int, input().split())
    p.append((l, r))
rs = sum(a)
for i in range(len(p)):
    if p[i][0] <= rs <= p[i][1]:
        print(rs)
        return
    if p[i][0] > rs:
        print(p[i][0])
        return
print(-1)
