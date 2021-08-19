N = int(input())

syogen = []
for i in range(N):
    a = int(input())
    temp = [list(map(int, input().split())) for _ in range(a)]
    syogen.append([a, temp])

ans = 0

for h in range(2**N):
    flag = 0
    cnt = 0
    l = [0] * N
    for g in range(N):
        if h >> g & 1:
            l[g] = 1
    # print(l)
    for gg in range(N):
        if l[gg] == 1:
            temp_ = syogen[gg]
            # print(temp_)
            for n in range(temp_[0]):
                if l[temp_[1][n][0] - 1] == temp_[1][n][1]:
                    continue
                else:
                    flag = 1
                    break
        if flag == 1:
            break
        elif flag == 0 and gg == N - 1:
            # print(bin(h))
            ans = max(ans, sum(l))

print(ans)
