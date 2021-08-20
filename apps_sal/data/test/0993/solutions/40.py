from sys import stdin
input = stdin.readline
(n, m) = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
dicti = {0: 1}
sumi = 0
for i in range(n):
    sumi += arr[i]
    sumi = sumi % m
    dicti[sumi] = dicti.get(sumi, 0) + 1
answer = 0
for i in dicti:
    val = dicti[i]
    toadd = val * (val - 1)
    toadd = toadd // 2
    answer += toadd
print(answer)
