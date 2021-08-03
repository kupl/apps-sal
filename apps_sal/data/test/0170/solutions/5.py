n = int(input())
sol_1 = list(map(int, input().split()))
l1 = sol_1[0]
s1 = l1
sol_1 = sol_1[1:]
sol_2 = list(map(int, input().split()))
l2 = sol_2[0]
s2 = l2
sol_2 = sol_2[1:]
i = 0
j = 0
sol_11 = []
sol_22 = []
p = 10000
c = 0
while s1 != 0 and s2 != 0 and p > 0:
    if i == len(sol_1):
        i = 0
        sol_1 = sol_11[:]
        sol_11 = []
    if j == len(sol_2):
        j = 0
        sol_2 = sol_22[:]
        sol_22 = []
    if sol_1[i] > sol_2[j]:
        sol_11.append(sol_2[j])
        sol_11.append(sol_1[i])
        s1 += 1
        s2 -= 1
    else:
        sol_22.append(sol_1[i])
        sol_22.append(sol_2[j])
        s2 += 1
        s1 -= 1
    i += 1
    j += 1
    c += 1
    p -= 1
if p == 0:
    print(-1)
else:
    if s1 == 0:
        print(c, '2')
    else:
        print(c, '1')
