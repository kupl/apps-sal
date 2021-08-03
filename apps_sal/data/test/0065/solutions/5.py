n = int(input())
l = list(map(int, input().split()))
x = min(l)
ls = []
for i in range(n):
    if l[i] == x:
        ls.append(i)
ans = n + 1
for i in range(len(ls) - 1):
    ans = min(ans, ls[i + 1] - ls[i])
print(ans)
