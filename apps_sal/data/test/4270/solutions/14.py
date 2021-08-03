N = int(input())
v = list(map(int, input().split()))

vs = sorted(v)
alc = 0
for i in range(N):
    if alc == 0:
        alc = vs[0]
    else:
        alc = (alc + vs[i]) / 2
print(alc)
