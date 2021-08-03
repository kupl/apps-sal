from sys import stdin, stdout
input = stdin.readline
#print = stdout.write

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    have = n
    for i in range(k - 1):
        digits = list(map(int, str(have)))
        bf = min(digits) * max(digits)
        if bf == 0:
            break
        have += bf
    print(have)
