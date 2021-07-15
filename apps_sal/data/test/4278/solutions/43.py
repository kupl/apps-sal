from collections import Counter
N = int(input())
s = [str(sorted(input())) for _ in range(N) ]
c = Counter(s)
cnt = []

for i in list(c.values()):
    cnt.append(i * (i -1)//2)
print((sum(cnt)))


