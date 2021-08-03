A, B, C = map(int, input().split())
lst = [A, B, C]
lst.sort()

ans = 0
if((lst[1] - lst[0]) % 2 == 0):
    ans += (lst[1] - lst[0]) // 2 + lst[2] - lst[1]
else:
    if((lst[2] - lst[0]) % 2 != 0):
        ans += (lst[2] - lst[1]) // 2 + (lst[2] + 1 - lst[0]) // 2 + 1
    elif((lst[2] - lst[1]) % 2 != 0):
        ans += (lst[2] - lst[0]) // 2 + (lst[2] + 1 - lst[1]) // 2 + 1
print(ans)
