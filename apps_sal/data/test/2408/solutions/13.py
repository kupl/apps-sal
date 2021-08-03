from collections import Counter
n = int(input())
l = set()
s = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = s[i]
        x2, y2 = s[j]
        if x1 == x2:
            l.add((float('INF'), x1))
        else:
            a = (y1 - y2) / (x1 - x2)
            b = (x1 * y2 - x2 * y1) / (x1 - x2)
            l.add((a, b))
lis = [i[0] for i in l]
dic = Counter(lis)
r = len(l)**2 - len(l)
for i in dic:
    r -= dic[i]**2 - dic[i]
print(r // 2)
