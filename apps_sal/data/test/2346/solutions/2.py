import sys

n = int(sys.stdin.readline().strip())
R = [0] * n

for i in range (0, n):
    line = sys.stdin.readline().strip().split()
    p = int(line[0])
    c = int(line[1])
    if c == 0:
        R[i] = 1
        if p != -1:
            R[p - 1] = 1

ans = [0] * (n - sum(R))
j = 0
for i in range (0, n):
    if R[i] == 0:
        ans[j] = str(i + 1)
        j = j + 1
ans = " ".join(ans)

if ans == "":
    print(-1)
else:
    print(ans)
