ans = []
for _ in range(int(input())):
    n = int(input())
    u = list(map(int, list(input())))
    cnt1 = cnt0 = 0
    for i in range(1, n):
        if u[i] == u[i - 1]:
            if u[i] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
    ans.append(max(cnt1, cnt0))
print(*ans, sep='\n')

