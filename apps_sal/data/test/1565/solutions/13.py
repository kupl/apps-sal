n = int(input())
s = input()
good = []
for i in range(1, n):
    if(s[i] != '0'):
        good.append([max(n - i, i), i])
good = sorted(good)
if len(good) == 0:
    good.append([n - 1, n - 1])
ans = int(s[:good[0][1]:]) + int(s[-(n - good[0][1]):])
for i in range(0, min(len(good), 3)):
    ans = min(ans, int(s[:good[i][1]:]) + int(s[-(n - good[i][1]):]))
print(ans)
