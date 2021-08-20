from sys import stdin
num = int(stdin.readline())
inp = list(map(int, stdin.readline().split()))
max = 0
localmax = 0
old = -1
for i in inp:
    if i > old:
        old = i
        localmax += 1
    else:
        old = i
        localmax = 1
    if localmax > max:
        max = localmax
print(max)
