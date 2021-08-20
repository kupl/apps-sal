import sys
(N, p) = list(map(int, input().split()))
l = list()
r = list()
for i in range(0, N):
    (a, b) = list(map(int, input().split()))
    l.append(a)
    r.append(b)
l.append(l[0])
r.append(r[0])
answer = 2000 * N
answer = 0
for i in range(0, N):
    c1 = l[i] // p
    c2 = r[i] // p
    pos1 = c2 - c1
    if l[i] % p == 0:
        pos1 += 1
    total1 = r[i] - l[i] + 1
    bad_pos1 = total1 - pos1
    c1 = l[i + 1] // p
    c2 = r[i + 1] // p
    pos2 = c2 - c1
    if l[i + 1] % p == 0:
        pos2 += 1
    total2 = r[i + 1] - l[i + 1] + 1
    bad_pos2 = total2 - pos2
    answer += 2000 * (1 - bad_pos1 / total1 * bad_pos2 / total2)
print(answer)
