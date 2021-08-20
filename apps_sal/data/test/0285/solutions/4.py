def rline():
    return [int(i) for i in input().split()]


N = int(input())
(L, R) = rline()
l = [rline() for i in range(N)]
atL = []
atR = []
for i in range(N):
    (k, b) = l[i]
    atL.append((k * L + b, k, i))
    atR.append((k * R + b, -k, i))
atL.sort()
atR.sort()
atL = [i[2] for i in atL]
atR = [i[2] for i in atR]
print(['YES', 'NO'][atL == atR])
