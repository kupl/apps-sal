n, x = [int(s) for s in input().split()]
a_list = [int(s) for s in input().split()]
ans = 0
temp = a_list[0] - x
if temp > 0:
    ans += temp
    a_list[0] -= temp
for i in range(1, n):
    temp = a_list[i] + a_list[i - 1] - x
    if temp > 0:
        ans += temp
        a_list[i] -= temp
print(ans)
