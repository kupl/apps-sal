n = int(input())
k = [True] * n
a = input().split()
num = {}
line = []
sweeping = []
for i in range(n):
    try:
        line.append([num[a[i]], i])
    except:
        num[a[i]] = i
line.sort()
if len(line) > 0:
    sweeping.append(line[0])
for i in line:
    start = i[0]
    end = i[1]
    if start > sweeping[-1][1]:
        sweeping.append(i)
    elif start <= sweeping[-1][1] and end > sweeping[-1][1]:
        sweeping[-1][1] = end
if len(sweeping) == 0:
    n -= 1
    ans = 1
    for i in range(n):
        ans *= 2
        ans %= 998244353
else:
    ans = 1
    for i in range(sweeping[0][0]):
        ans *= 2
    for i in range(1, len(sweeping)):
        for j in range(sweeping[i][0] - sweeping[i - 1][1]):
            ans *= 2
            ans %= 998244353
    for i in range(n - sweeping[-1][1] - 1):
        ans *= 2
        ans %= 998244353
print(ans)
