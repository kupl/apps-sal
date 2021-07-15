n = int(input())
l = list(map(int,input().split()))
l.sort()
if sum(l[0:n-1]) > l[n-1]:
    print('Yes')
else:
    print('No')
