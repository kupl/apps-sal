import sys

s = sys.stdin.readline().strip()
if s[0] != '0':
    s = '0'+ s

ans = [[[10**9 for i in range (0, 10)] for j in range (0, 10)] for k in range (0, 10)]

for n in range (0, 20):
    for i in range (0, 10):
        for j in range (0, 10):
            for k in range (0, 10):
                if (k == i or k == j):
                    ans[i][j][k] = 1
                else:
                    ans[i][j][k] = min([ans[i][j][k], 1+ans[i][j][(k-i+10)%10], 1+ans[i][j][(k-j+10)%10]])

x = [0] * 10
for i in range (0, len(s)-1):
    x[(int(s[i+1])-int(s[i])+10)%10] = x[(int(s[i+1])-int(s[i])+10)%10] + 1


for i in range (0, 10):
    ans2 = [0] * 10
    for j in range (0, 10):
        for k in range (0, 10):
            ans2[j] = ans2[j] + (ans[i][j][k]-1) * x[k]
        if ans2[j] >= 10 ** 8:
            ans2[j] = -1
    print(" ".join(list(map(str,ans2))))

