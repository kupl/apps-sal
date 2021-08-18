from sys import stdin
N = int(stdin.readline().rstrip())
D = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
doublets = 0
for d in D:
    if d[0] == d[1]:
        doublets += 1
    else:
        doublets = 0
    if doublets >= 3:
        print("Yes")
        return
print("No")
