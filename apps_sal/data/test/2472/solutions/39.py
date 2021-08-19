n = int(input())
t = []
for i in range(n):
    (a, b) = map(int, input().split())
    t.append([b, a])
t.sort()
p = 0
ans = 'Yes'
for i in range(n):
    p += t[i][1]
    if p > t[i][0]:
        ans = 'No'
        break
print(ans)
