n = int(input())
a = list(map(int, [input() for i in range(n)]))
ans = 1
hikari = 1
for i in range(n):
        hikari = a[hikari -1]
        if hikari == 2:
                print(ans)
                return
        else:
                ans  += 1
print(-1)
