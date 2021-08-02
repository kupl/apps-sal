n = int(input())
p = list(map(int, input().split()))

q = p.copy()
q.sort()

counter = 0
for i in range(n):
    if p[i] != q[i]:
        counter += 1

if counter == 0 or counter == 2:
    print('YES')
else:
    print('NO')
