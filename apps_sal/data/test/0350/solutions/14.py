n = int(input())
ai = list(map(int, input().split()))
ai.sort()
ai.reverse()
last_num = ai[0] + 1
ans = 0
for num in ai:
    if last_num == 0:
        break
    if num >= last_num:
        last_num -= 1
    else:
        last_num = num
    ans += last_num
print(ans)
