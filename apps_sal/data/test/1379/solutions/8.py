from operator import itemgetter
n, m, d = map(int, input().split())
ai = list(map(int, input().split()))
ai2 = [[ai[i], i] for i in range(n)]
d += 1
ai2.sort(key=itemgetter(0))
ai4 = [0] * n
ai5 = [0] * n
ai4[0] = ai2[0][0]
ai5[0] = 1
ai[ai2[0][1]] = 1
j = 1
i = 1
z = 0
while i < n:
    if ai2[i][0] < ai4[z] + d:
        ai4[j + z] = ai2[i][0]
        ai5[j + z] = j + 1
        j += 1
        ai[ai2[i][1]] = j
    else:
        ai4[j + z] = ai2[i][0]
        ai5[j + z] = ai5[z]
        ai[ai2[i][1]] = ai5[z]
        z += 1
    i += 1
print(j)
for i in range(n):
    print(ai[i], end=" ")
