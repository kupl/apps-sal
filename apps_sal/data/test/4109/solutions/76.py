import numpy as np

N, M, X = map(int, input().split())
books = []
for i in range(N):
    tmp_book = list(map(int, input().split()))
    books.append(tmp_book)

ans = 10**10
for i in range(1, 2**(N)):
    flag = 1
    tmp = str(bin(i))
    if len(tmp[2:]) < N:
        tmp = '0' * (N - len(tmp[2:])) + tmp[2:]
    else:
        tmp = tmp[2:]
    ability = np.zeros(M)
    money = 0
    for j in range(N):
        if tmp[j] == '1':
            ability += books[j][1:]
            money += books[j][0]
    # print(ability)
    for j in range(M):
        if ability[j] < X:
            flag = 0
            break
    if flag == 1:
        ans = min(ans, money)
if ans == 10**10:
    print(-1)
else:
    print(ans)
