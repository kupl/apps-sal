y = [int(i) for i in input().split()]

N = y[0]
Q = y[1]

if(Q == 0):
    print(N)
    return
y = [int(i) for i in input().split()]
# y.append(N)
ans = []

for i in range(102):
    if i in y:
        continue
    ans.append(i)

for i in range(0, -102, -1):
    if i in y:
        continue
    ans.append(i)

t = abs(N - ans[0])
anss = 0
for i in ans:
    if (abs(N - i) < t):
        anss = i
        t = abs(i - N)

print(anss)
