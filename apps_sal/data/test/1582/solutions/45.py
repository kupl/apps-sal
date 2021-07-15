from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(1, n+1):
    if str(i)[-1] == '0':
        continue
    d[int(str(i)[0] + str(i)[-1])] += 1
ans = 0
for i in range(11, 100):
    ans += d[i] * d[int(str(i)[1] + str(i)[0])]
print(ans)
