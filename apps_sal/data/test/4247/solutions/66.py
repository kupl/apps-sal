n = int(input())
perm_list = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    a = perm_list[i]
    b = perm_list[i + 1]
    c = perm_list[i + 2]
    if a < b < c or c < b < a:
        ans += 1
print(ans)
