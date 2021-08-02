N = int(input())
Cls = [0]
Sls = [0]
Fls = [0]
lsans = []
for i in range(1, N):
    c, s, f = map(int, input().split())
    Cls.append(c)
    Sls.append(s)
    Fls.append(f)
for i in range(1, N):
    t = 0
    for j in range(i, N):
        if t < Sls[j]:
            t = Sls[j] + Cls[j]
        elif t % Fls[j] == 0:
            t += Cls[j]
        else:
            t += Fls[j] - (t % Fls[j]) + Cls[j]
    lsans.append(t)
lsans.append(0)
for i in lsans:
    print(i)
