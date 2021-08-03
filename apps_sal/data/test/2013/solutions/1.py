n, m, k = list(map(int, input().split()))
s = list(map(int, input().split()))
f = list(map(int, input().split()))
ans = ""
for i in range(n - 1):
    ans += "U"
for i in range(m - 1):
    ans += "L"
for i in range(n):
    if i % 2 == 0:
        ans += ("R" * (m - 1))
    else:
        ans += ("L" * (m - 1))
    if i != n - 1:
        ans += "D"
print(len(ans))
print(ans)
