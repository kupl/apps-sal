n = int(input())
list_w = [int(i) for i in input().split()]
tmp1 = 0
tmp2 = 0
ans = sum(list_w)
for i in range(0, len(list_w)):
    tmp1 = sum(list_w[:i + 1])
    tmp2 = sum(list_w[i + 1:])
    if ans > abs(tmp1 - tmp2):
        ans = abs(tmp1 - tmp2)
print(ans)
