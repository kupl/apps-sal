(n, a) = list(map(int, input().split()))
l = input().split()
l = [int(i) for i in l]
if n == 1:
    print(0)
elif n == 2:
    if abs(a - l[0]) < abs(a - l[1]):
        print(abs(a - l[0]))
    else:
        print(abs(a - l[1]))
else:
    ma = max(l)
    mi = min(l)
    l.remove(ma)
    max2 = max(l)
    l.append(ma)
    l.remove(mi)
    min2 = min(l)
    l.append(mi)
    if a > ma:
        print(a - min2)
    elif a < mi:
        print(max2 - a)
    else:
        ans = list()
        ans.append(abs(max2 - a) + max2 - mi)
        ans.append(abs(a - mi) + max2 - mi)
        ans.append(ma - min2 + abs(ma - a))
        ans.append(ma - min2 + abs(a - min2))
        while min(ans) < 0:
            ans.remove(min(ans))
        print(min(ans))
