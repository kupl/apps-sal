S = list(input())
K = int(input())
lsS = [int(i) for i in S]
ii = 0
for i in range(len(S)):
    if lsS[i] == 1:
        ii += 1
    else:
        a = lsS[i]
        break
if ii >= K:
    print(1)
else:
    print(a)
