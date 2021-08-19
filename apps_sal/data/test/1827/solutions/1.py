n = int(input())
a = list(map(int, input().split()))
# if n==1:
#    print(a[0])
#    return
for i in range(n):
    b = max(a)
    c = min(a)
    print(b, c)
    a.remove(b)
    a.remove(c)
