n,k = (int(x) for x in input().split(' '))
a = [int(x) for x in input().split(' ')]
a.sort()
ans = sum(a[0:k])
print(ans)
