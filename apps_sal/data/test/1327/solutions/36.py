(N, M) = map(int, input().split())
X = []
Y = []
Z = []
G1 = []
G2 = []
G3 = []
G4 = []
G5 = []
G6 = []
G7 = []
G8 = []
for i in range(N):
    (x, y, z) = map(int, input().split())
    G1.append(-(x + y + z))
    G2.append(-(x + y) + z)
    G3.append(-x + y - z)
    G4.append(-x + (y + z))
    G5.append(x - (y + z))
    G6.append(x - y + z)
    G7.append(x + y - z)
    G8.append(x + y + z)
G1.sort(reverse=True)
G2.sort(reverse=True)
G3.sort(reverse=True)
G4.sort(reverse=True)
G5.sort(reverse=True)
G6.sort(reverse=True)
G7.sort(reverse=True)
G8.sort(reverse=True)
ans = 0
val1 = 0
val2 = 0
val3 = 0
val4 = 0
val5 = 0
val6 = 0
val7 = 0
val8 = 0
for i in range(M):
    val1 += G1[i]
    val2 += G2[i]
    val3 += G3[i]
    val4 += G4[i]
    val5 += G5[i]
    val6 += G6[i]
    val7 += G7[i]
    val8 += G8[i]
ans = max(val1, val2, val3, val4, val5, val6, val7, val8)
print(ans)
