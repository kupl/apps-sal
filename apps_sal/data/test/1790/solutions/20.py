from sys import stdin
n = int(stdin.readline().strip())

s = set(list(map(int, stdin.readline().strip().split()))[1::])
for i in range(n - 1):
    s1 = set(list(map(int, stdin.readline().strip().split()))[1::])
    s2 = set()
    for i in s1:
        if i in s:
            s2.add(i)
    s = s2.copy()
print(*list(s))
