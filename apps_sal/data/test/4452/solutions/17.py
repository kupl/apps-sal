from sys import stdin, stdout
#input = stdin.readline
#print = stdout.write

for _ in range(int(input())):
    x = input()
    res = []
    for ind, i in enumerate(x):
        if i != '0':
            res.append(i + '0' * (len(x) - ind - 1))
    print(len(res))
    print(*res)
