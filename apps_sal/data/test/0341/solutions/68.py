(N, K) = map(int, input().split())
(R, S, P) = map(int, input().split())
d = {'r': P, 's': R, 'p': S}
T = input()
ans = 0
for i in range(min(N, K)):
    flag = 0
    tmp = T[i::K]
    for j in range(len(tmp) - 1):
        if tmp[j] != tmp[j + 1] or flag:
            ans += d[tmp[j]]
            flag = 0
        else:
            flag = 1
    ans += d[tmp[-1]]
print(ans)
