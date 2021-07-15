from collections import Counter
n = int(input())
m = []
count = 0
for i in range(n):
    m.append("".join(sorted(str(input()))))
m = Counter(m)
ans = 0
for j in m.values():
    ans += j * (j-1) / 2
print(int(ans))
