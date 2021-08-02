n = int(input())
a_l = list(map(int, input().split()))
m = 1
for a in a_l:
    m *= a
ans = 0
for a in a_l:
    ans += (m - 1) % a
print(ans)
