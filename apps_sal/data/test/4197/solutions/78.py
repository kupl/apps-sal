n = int(input())
lst = list(map(int, input().split()))
lst2 = [0 for i in range(n)]
for i in range(n):
    x = lst[i]
    lst2[x - 1] = i + 1
for i in range(n):
    if i != n - 1:
        print(lst2[i], end=' ')
    else:
        print(lst2[i])
