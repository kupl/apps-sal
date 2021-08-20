from sys import stdin, stdout
n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
v = max(values)
sze = 25
stdout.write(str(max(0, v - sze)))
