import itertools
N, M = map(int, input().split())
Switch = []
for i in range(M):
    Swi = list(map(int, input().split()))
    S = Swi[0]
    Switch.append(Swi[1:S + 1])
Plist = list(map(int, input().split()))
Ans = 0
L = [0, 1]
c_list = list(itertools.product(L, repeat=N))
for comb in c_list:
    for i in range(M):
        Jud = 0
        Swi = Switch[i]
        for j in Swi:
            Jud += comb[j - 1]
        if Jud % 2 != Plist[i]:
            break
        elif i == M - 1:
            Ans += 1
print(Ans)
