from math import ceil
n = int(input())
apna = list(map(int, input().split()))
unka = list(map(int, input().split()))
cnt = 0
c = 0
for i in range(n):
    if unka[i] == 1 and apna[i] == 0:
        cnt += 1
    if apna[i] == 1 and unka[i] == 0:
        c += 1
cnt += 1
if cnt > 0 and c == 0:
    print(-1)
else:
    print(ceil(cnt / c))
