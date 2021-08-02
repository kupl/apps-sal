n = int(input())
a = [int(s) for s in input().split()]
for i in a:
    if i % 2 == 0:
        print(i - 1, end=' ')
    else:
        print(i, end=' ')
