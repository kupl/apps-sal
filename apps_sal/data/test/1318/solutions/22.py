n = int(input())
requests = []
i = 0
while i != n:
    (c, p) = [int(x) for x in input().split()]
    requests.append((p, c, i + 1))
    i += 1
k = int(input())
R = input().split()
r = []
for x in range(len(R)):
    r.append((int(R[x]), x + 1))
m = s = 0
accepted = []
reserved = [0 for _ in range(n)]
maxx = (0, 0, 0)
reverse_sorted_requests = list(reversed(sorted(requests)))
for j in sorted(r):
    for i in reverse_sorted_requests:
        if maxx[2] == 0 and i[1] <= j[0] and (not reserved[i[2] - 1]):
            maxx = i
        elif i[0] > maxx[0] and i[1] <= j[0] and (not reserved[i[2] - 1]):
            maxx = i
    if maxx[2] != 0:
        accepted.append((maxx[2], j[1]))
        reserved[maxx[2] - 1] = 1
        m += 1
        s += maxx[0]
        reverse_sorted_requests.remove(maxx)
        maxx = (0, 0, 0)
print(m, s)
for a in accepted:
    print(a[0], a[1])
