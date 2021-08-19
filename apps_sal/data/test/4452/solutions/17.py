from sys import stdin, stdout
for _ in range(int(input())):
    x = input()
    res = []
    for (ind, i) in enumerate(x):
        if i != '0':
            res.append(i + '0' * (len(x) - ind - 1))
    print(len(res))
    print(*res)
