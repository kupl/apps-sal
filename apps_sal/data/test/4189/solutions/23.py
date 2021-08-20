n = int(input())
s = 0
h = 0
for i in range(n):
    (a, b) = input().split()
    if b == 'soft':
        s += 1
    else:
        h += 1
mx = max(s, h)
mn = min(s, h)
pq = [(1, 0), (2, 2), (5, 4), (8, 8), (13, 12), (18, 18), (25, 24), (32, 32), (41, 40), (50, 50), (61, 60), (72, 72), (85, 84), (98, 98), (113, 112)]
for i in range(len(pq)):
    if mx <= pq[i][0] and mn <= pq[i][1]:
        print(i + 1)
        break
