from itertools import product
n = int(input())
test = []
for i in range(n):
    a = int(input())
    test.append([list(map(int, input().split())) for i in range(a)])
ans = 0
for i in product(range(2), repeat=n):
    flag = True
    for j in range(n):
        if i[j] == 1:
            for s in test[j]:
                if i[s[0] - 1] != s[1]:
                    flag = False
                    break
    if flag == True:
        cnt = i.count(1)
        if cnt > ans:
            ans = cnt
print(ans)
