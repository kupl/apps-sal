n = int(input())
lst = list(map(int, input().split()))

if lst[0] > lst[1]:
    di = 1

else:
    di = -1

ans = 0
now = lst[1]

for i in range(2, n):
    if di == 1 and now > lst[i]:
            ans += 1

    elif di == -1 and now < lst[i]:
            ans += 1

    else:
        di = -di

    now = lst[i]

print(ans)

