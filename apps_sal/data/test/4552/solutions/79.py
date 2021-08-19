N = int(input())
F = [0] * N
for i in range(N):
    F[i] = list(map(int, input().split()))

P = [0] * N
for i in range(N):
    P[i] = list(map(int, input().split()))

#print(F, P)
#print(4 >> 1)
ans = - 10 ** 10
# print(ans)
for i in range(1, 2 ** 10):  # bit全探索 #0は空いてる時間帯がないのでカット
    open_n = [0] * N
    profit = 0
    for j in range(10):  # 10240通り
        if ((i >> j) & 1):  # jの時間帯に空いてる
            for k in range(N):  # 100
                if F[k][j] == 1:
                    open_n[k] += 1
    for l in range(N):
        profit += P[l][open_n[l]]
    if ans < profit:
        ans = profit

print(ans)
