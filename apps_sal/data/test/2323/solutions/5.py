import sys

n = int(sys.stdin.readline().strip())
ans = []
s = list(map(int, sys.stdin.readline().strip().split()))
s.sort()
t = [0] * n
c = [0] * (n + 1)
for i in range (0, n - 1):
    t[i] = s[i + 1] - s[i]
t[n - 1] = 10 ** 18 + 1
t.sort()
for i in range (0, n):
    c[i + 1] = c[i] + t[i]
q = int(sys.stdin.readline().strip())
for i in range (0, q):
    line = sys.stdin.readline().strip().split()
    l = int(line[1]) - int(line[0]) + 1
    j1 = 0
    j2 = n
    j = (j1 + j2) // 2
    if t[0] > l:
        j1 = -1
    else:
        while j2 - j1 > 1:
            if t[j] <= l:
                j1 = j
            else:
                j2 = j
            j = (j1 + j2) // 2
    ans.append(str((c[j1 + 1] + (n - j1 - 1) * l)))
print(" ".join(ans))
