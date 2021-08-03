n = int(input())
L = [0] * 200
for i in range(1, n + 1, 2):
    tmp = 1
    cnt = 0
    while tmp <= i:
        if i % tmp == 0:
            cnt += 1
        tmp += 1
        L[i] = cnt
print(L.count(8))
