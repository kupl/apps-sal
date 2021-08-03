n = int(input())
CompS = []
S = 0
for i in range(n):
    m, *H = list(map(int, input().split()))
    Max = max(H)
    CompS.append((Max, m))
CompS.sort(reverse=True)

for i in range(1, len(CompS)):
    S += (CompS[0][0] - CompS[i][0]) * CompS[i][1]
print(S)
