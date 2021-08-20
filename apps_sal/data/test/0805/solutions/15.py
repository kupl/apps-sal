from sys import stdin, stdout
n = int(stdin.readline().strip())
alex = list(map(int, stdin.readline().strip().split()))
alex_lst = list(range(alex[0] + 1, alex[1] + 1))
for i in range(1, n):
    lst = list(map(int, stdin.readline().strip().split()))
    for j in range(lst[0] + 1, lst[1] + 1):
        if j in alex_lst:
            alex_lst.remove(j)
stdout.write(str(len(alex_lst)))
