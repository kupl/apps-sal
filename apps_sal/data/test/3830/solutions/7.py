from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    n = int(input())
    s = input()
    s = s[:n]
    if s.count('>') == 0 or s.count('<')==0:
        print(n)
    else:
        wyn = 0
        dasie = [0] * n
        for i in range(n):
            if s[i] == '-':
                dasie[i] = 1
            if s[i-1] == '-':
                dasie[i] = 1
        print(sum(dasie))
