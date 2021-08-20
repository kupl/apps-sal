l = input().split()
n = int(l[0])
m = int(l[1])
vs = []
for i in range(n):
    vs.append(int(input()))
vs.append(10 ** 9)
vs.sort()
hs = []
for i in range(m):
    l = input().split()
    if int(l[0]) == 1:
        hs.append(int(l[1]))
hs.sort()
j = 0
mina = 10 ** 9
for i in range(n + 1):
    if j < len(hs):
        while hs[j] < vs[i]:
            j += 1
            if j == len(hs):
                break
    if i + len(hs) - j < mina:
        mina = i + len(hs) - j
print(mina)
