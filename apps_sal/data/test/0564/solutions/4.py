n, s = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
l.sort()
if sum(l[:-1]) <= s:
    print("YES")
else:
    print("NO")
