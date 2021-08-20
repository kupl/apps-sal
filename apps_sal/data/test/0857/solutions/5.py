(n, n) = map(int, input().split())
lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]
for x in lst1:
    if x in lst2:
        print(x, end=' ')
