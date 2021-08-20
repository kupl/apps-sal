import sys
fin = sys.stdin
n = int(fin.readline())
file = [None] * n
disk = tuple(map(int, input().split()))
for i in range(n):
    file[disk[i] - 1] = i
ctime = 0
for i in range(1, n):
    ctime += abs(file[i] - file[i - 1])
print(ctime)
