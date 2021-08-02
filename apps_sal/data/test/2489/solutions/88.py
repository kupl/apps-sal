n = int(input())
a = list(map(int, input().split()))
m = max(a)
flag = [True] * (m + 1)
c = [0] * (m + 1)
b = list(sorted(a))
for i in b:
    x = i + i
    while x <= m:
        flag[x] = False
        x += i
    c[i] += 1
ans = 0
x = 0
l = []
ans = 0
for i in a:
    if flag[i] and c[i] <= 1:
        ans += 1
print(ans)
