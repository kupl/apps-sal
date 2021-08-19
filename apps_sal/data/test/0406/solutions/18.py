s = input()
lst = [int(i) for i in input().split()]
lst.sort()
lst = lst[::-1]
n = 0
k = 0
while len(lst) >= 2:
    if lst[0] == lst[1] or lst[0] == lst[1] + 1:
        if k != 0:
            n += k * lst[1]
            lst.pop(0)
            lst.pop(0)
            k = 0
        else:
            k = lst[1]
            lst.pop(0)
            lst.pop(0)
    else:
        lst.pop(0)
print(n)
