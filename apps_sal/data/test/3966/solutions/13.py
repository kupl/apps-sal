def sum_l(lst):
    temp = 0
    for i in lst:
        temp += i
    return temp


l1 = input()
l1 = int(l1)
a = input()
l2 = [int(x) for x in a.split()]
l2.sort()
ans = 0
if len(l2) == 1:
    ans += l2[0]
else:
    n = 0
    for i in l2:
        ans += i * (n + 2)
        n += 1
    ans -= l2[-1]
print(ans)
