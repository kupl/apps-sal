n = int(input())
li = list(map(int,input().split()))

li.sort()

su = sum(li)
if li[n-1] < su - li[n-1]:
    print('Yes')
else:
    print('No')
