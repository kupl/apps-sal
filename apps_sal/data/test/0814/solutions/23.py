n = input()
columns = [int(x) for x in input().split()]
for x in sorted(columns):
    print(x, end=' ')
