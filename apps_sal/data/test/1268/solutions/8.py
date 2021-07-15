n=int(input())
l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
l2.sort()
if sum(l1)<=(l2[-1]+l2[-2])  :
    print("YES")
else:
    print("NO")
