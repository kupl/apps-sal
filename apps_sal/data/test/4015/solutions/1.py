n, m = map(int, input().split())
if m % n:
    print(-1)
    return
m //= n
a = 0
while m % 2 == 0:
    m//=2
    a+=1
while m % 3 == 0:
    m//=3
    a+=1
if m==1:
    print(a)
else:
    print(-1)
