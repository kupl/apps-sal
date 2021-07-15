x = int(input())
ans = int((x * 2) ** 0.5)
while 1:
    if ans * (ans + 1) // 2 >= x:
        print(ans)
        break
    ans += 1
