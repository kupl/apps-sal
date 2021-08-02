from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    s, i, e = [int(i) for i in input().split()]

    x = (i + e - s) // 2

    if x < 0:
        print(e + 1)
    elif x > e:
        print(0)
    else:
        print(e - x)
