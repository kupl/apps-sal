from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))
    print(a ^ b)
