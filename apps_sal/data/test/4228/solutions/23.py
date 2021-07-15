n, l = map(int, input().split())
a = [l+i for i in range(n)]
if 0 in a:
    print(sum(a))
elif a[0] < 0:
    print(sum(a)-a[-1])
else:
    print(sum(a)-a[0])
