n = int(input())
t = [int(s) for s in input().split()]
m = int(input())
total = sum(t)
ans = []
for i in range(m):
    p, x = map(int, input().split())
    ans.append(total - t[p - 1] + x)

for a in ans:
    print(a)
