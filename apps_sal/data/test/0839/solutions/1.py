import random
import sys
a = [[0] * 5 for i in range(5)]
a[0] = list(map(int, input().split()))
a[1] = list(map(int, input().split()))
a[2] = list(map(int, input().split()))
a[3] = list(map(int, input().split()))
a[4] = list(map(int, input().split()))
ans = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for s in range(5):
                    if i == j or i == k or i == l or i == s or j == k or j == l or j == s or k == l or k == s or l == s:
                        continue
                    ans = max(ans, a[i][j] + a[j][i] + a[k][l] + a[l][k] + a[j][k] + a[k][j] + a[l][s] + a[s][l] + a[k][l] + a[l][k] + a[l][s] + a[s][l])
print(ans)
