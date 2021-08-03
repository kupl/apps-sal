import sys
input = sys.stdin.readline


n, k = list(map(int, input().split()))

SUSHI = []
for _ in range(n):
    t, d = list(map(int, input().split()))
    SUSHI.append((d, t))
SUSHI.sort(reverse=True)

NEW = {i: True for i in range(1, n + 1)}
x, y = 0, 0
A, B = [], []

for d, t in SUSHI[:k]:
    if NEW[t]:
        x += d
        y += 1
        NEW[t] = False
    else:
        x += d
        A.append(d)

for d, t in SUSHI[k:]:
    if NEW[t]:
        B.append(d)
        NEW[t] = False
B.sort()

answer = x + y**2
while A and B:
    a, b = A.pop(), B.pop()
    x -= a
    x += b
    y += 1
    if x + y**2 > answer:
        answer = x + y**2

print(answer)
