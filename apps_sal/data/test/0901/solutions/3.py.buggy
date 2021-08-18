import sys

n, m = list(map(int, input().split()))

for _ in range(m):
    l = [int(x) for x in input().split()][1:]
    s = set(l)
    ok = False
    for i in l:
        if -i in s:
            ok = True
            break
    if not ok:
        print("YES")
        return

print("NO")
