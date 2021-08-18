n = int(input())

lst1 = 1
lst2 = 1

cnt = 0

while (True):
    cnt += 1
    lst1, lst2 = lst2, lst1
    if (lst1 + lst2 == n):
        print(cnt)
        return
    if (lst1 + lst2 > n):
        print(cnt - 1)
        return
    lst2 = lst1 + lst2
