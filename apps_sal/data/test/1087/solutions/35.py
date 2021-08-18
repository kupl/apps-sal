N, K = map(int, input().split())

A = list(map(int, input().split()))
MAX = max(max(A), K)
l = len(str(bin(MAX))) - 2

AB = []
for i in range(N):
    s = str(bin(A[i]))
    temp = s[2:]
    lendif = l - len(temp)
    while lendif > 0:
        temp = "0" + temp
        lendif -= 1
    AB.append(temp)

ans = 0
now = 0
for i in range(l):
    c = 0
    d = 0
    for j in range(N):
        if AB[j][i] == "0":
            c += 1
        else:
            d += 1
    if c > d:
        if pow(2, l - 1 - i) + now > K:
            m = d
        else:
            now += pow(2, l - 1 - i)
            m = c
    else:
        m = d
    ans += pow(2, l - 1 - i) * m
print(ans)
