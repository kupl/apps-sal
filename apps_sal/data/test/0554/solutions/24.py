(n, m) = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
for i in range(m):
    (li, ri) = map(int, input().split())
    li -= 1
    if sum(data[li:ri]) > 0:
        ans += sum(data[li:ri])
print(ans)
