from sys import stdin

n = int(stdin.readline())
a = [int(o) for o in stdin.readline().split()]

inv = len([1 for i in range(n) for j in range(i + 1, n) if a[i] > a[j]])
ans = inv % 2

m = int(stdin.readline())

for i in range(m):
    line = stdin.readline().split()
    l = int(line[0])
    r = int(line[1])

    v = ((r - l + 1) * (r - l) // 2) % 2
    ans ^= v

    if ans == 0:
        print("even")

    else:
        print("odd")
