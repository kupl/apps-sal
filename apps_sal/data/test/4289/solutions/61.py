n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
tmp = []

for i in range(n):
    x = t - h[i] * 0.006
    if a >= x:
        TMP = a - x
        tmp.append(TMP)
    else:
        TMP = x - a
        tmp.append(TMP)

for i in range(n):
    if tmp[i] == min(tmp):
        print(i+1)
