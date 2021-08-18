[N, M] = [int(i) for i in input().split()]
dic = {}
t = 0
for i in range(M):
    [s, c] = [int(i) for i in input().split()]
    if s in dic:
        if dic[s] != c:
            t += 1
            break
    else:
        dic[s] = c


for i in range(1, N + 1):
    if i not in dic:
        if i == 1:
            if N == 1:
                dic[1] = 0
            else:
                dic[1] = 1
        else:
            dic[i] = 0

if t == 0:
    if N == 1:
        print(dic[1])
    else:
        if dic[1] == 0:
            t += 1
        else:
            ans = 0
            for i in range(1, N + 1):
                ans += dic[i] * 10**(N - i)
            print(ans)

if t != 0:
    print('-1')
