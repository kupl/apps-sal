n = int(input())
a = list(map(int, input().split()))

s = sum(a)
count = {}
for x in a:
    count[x] = count.get(x, 0) + 1

q = int(input())
ans = []
for _ in range(q):
    b, c = map(int, input().split())
    s += (c - b) * count.get(b, 0)
    count[c] = count.get(c, 0) + count.get(b, 0)
    count[b] = 0
    ans.append(s)

for x in ans:
    print(x)
