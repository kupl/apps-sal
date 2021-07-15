n = int(input())
score = list(map(lambda x: [int(x), 0], input().split()))
m = int(input())    
score += list(map(lambda x: [int(x), 1], input().split()))
score.sort()
f = []
if score[0][1] == 0:
    f.append([1, 0])
else:
    f.append([0, 1])
for i in range(1, n + m):
    if score[i][1] == 0:
        f.append([f[i-1][0] + 1, f[i-1][1]])
    else:
        f.append([f[i-1][0], f[i-1][1] + 1])

a, b = f[-1][0] * 2, f[-1][1] * 2
aa, bb = f[-1][0] * 3, f[-1][1] * 3
if (aa - bb) > (a - b) or (aa - bb == a - b and aa > a):
    a, b = aa, bb
for i in range(n + m - 1):
    if score[i][0] != score[i+1][0]:
        aa = f[i][0] * 2 + (f[-1][0] - f[i][0]) * 3
        bb = f[i][1] * 2 + (f[-1][1] - f[i][1]) * 3
        if (aa - bb) > (a - b) or (aa - bb == a - b and aa > a):
            a, b = aa, bb
print(a, ':', b, sep='')            

