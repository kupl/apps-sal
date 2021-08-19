t = int(input())
lst = list(map(int, input().split()))
lst1 = list(map(int, input().split()))
for i in range(len(lst)):
    q = 0
    for j in range(i + 1):
        if lst[j] <= lst1[i]:
            q += lst[j]
            lst[j] = 0
        else:
            q += lst1[i]
            lst[j] -= lst1[i]
    print(q, end=' ')
