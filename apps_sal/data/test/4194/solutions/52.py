s = 0
n , m = list(map(int,input().split()))
a = list(map(int,input().split()))
for i in range(0 , len(a)):
    s = s + a [i]
if s > n:
    print((-1))
    return
print((n - s))

