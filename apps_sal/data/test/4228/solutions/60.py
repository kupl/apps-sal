n, l = map(int, input().split())
a = 0
if l >= 0:
    a = (l+1+n + l -1)*(n-1)/2
    print(int(a))

elif l < 0 and -l < n:
    a = (l+n + l -1)*n/2
    print(int(a))
elif l < 0 and -l >=n:
    a = (l+ n + l -2)*(n-1)/2
    print(int(a))
