from sys import stdin
n = int(stdin.readline().strip())
for i in range(n):
    s = list(map(int, stdin.readline().strip().split()))
    if s[0] > s[2]:
        print(s[2])
        continue
    x = s[1] // s[2]
    x += 1
    print(x * s[2])
