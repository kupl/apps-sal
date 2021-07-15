S = int(input())

if S < 3:
    print((0))
    return

ans = [0 for _ in range(2001)]

ans[3] = 1
ans[4] = 1
ans[5] = 1

for i in range(6, S+1):
    ans[i] = ans[i-3] + ans[i-1]

print((ans[S] % 1000000007))

