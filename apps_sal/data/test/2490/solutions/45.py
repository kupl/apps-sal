N = list(input())

num = 0
ans = 0
for i in range(len(N)-1, -1, -1):
    n = int(N[i])
    if n+num == 5 and i > 0 and int(N[i-1]) >= 5:
        ans += 5
        num = 1
    elif n+num < 6:
        ans += n+num
        num = 0
    else:
        ans += 10-(n+num)
        num = 1

ans += num
print(ans)
