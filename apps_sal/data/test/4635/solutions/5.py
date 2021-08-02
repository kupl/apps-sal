from sys import stdin
n1 = int(stdin.readline().strip())
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(n1):
    n, m = list(map(int, stdin.readline().strip().split()))
    x = 0
    s1 = ""
    for j in range(n):
        s1 += s[x]
        x += 1
        if (j + 1) % m == 0:
            x = 0
    print(s1)
