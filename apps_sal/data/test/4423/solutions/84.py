n = int(input())
s = [list(input().split()) for i in range(n)]
for i in range(n):
    s[i][1] = int(s[i][1])

q = sorted(s, key=lambda x: x[1])
q = sorted(q, key=lambda x: x[1], reverse=True)
q = sorted(q, key=lambda x: x[0])

for i in range(n):
    print(s.index(q[i]) + 1)
