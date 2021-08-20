N = int(input())
syougen = [[] for _ in range(N)]
for i in range(N):
    num = int(input())
    for j in range(num):
        (x, y) = map(int, input().split())
        syougen[i].append([x, y])
ans = 0
for bit in range(1 << N):
    break_flag = 0
    for i in range(N):
        if bit >> i & 1:
            for j in range(len(syougen[i])):
                if bit >> syougen[i][j][0] - 1 & 1 != syougen[i][j][1]:
                    break_flag = 1
                    break
            if break_flag == 1:
                break
        if i == N - 1:
            ans = max(ans, bin(bit).count('1'))
print(ans)
