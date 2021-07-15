n, a, b = list(map(int, input().split()))
l = []
ans = 0
for i in range(n):
    l.append(str(i + 1))
for i in l:
    li = list(map(int, i))
    if a <= sum(li) <= b:
        ans += int(i)
print(ans)

