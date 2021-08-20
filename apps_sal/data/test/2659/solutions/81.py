k = int(input())
n = 1
dif = 1
cnt = 0
while cnt != k:
    sn = 0
    for ele in str(n):
        sn += int(ele)
    m = n + dif
    sm = 0
    for ele in str(m):
        sm += int(ele)
    if n / sn <= m / sm:
        print(n)
        cnt += 1
        n += dif
    else:
        n -= dif
        dif *= 10
        n += dif
