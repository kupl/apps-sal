def sam(lst):
    return lst[1:] == lst[:-1]


n = int(input())
s = [int(x) for x in input().split()]
if(sam(s)):
    print(0)
else:
    x = round(sum(s) / n)
    n = 0
    for elem in s:
        n += (elem - x)**2
    print(n)
