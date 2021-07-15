n = int(input())
li = list(map(int,input().split()))
li.sort(reverse = True)
if n % 2 == 0:
    a = 0
    b = 0
    for i in range(int(n/2)):
        a += li[2*i]
        b += li[2*i+1]
    ans = a - b
    print(ans)
else:
    a = 0
    b = 0
    for i in range(int((n-1)/2)):
        a += li[2*i]
        b += li[2*i+1]
    ans = a + li[n-1] - b
    print(ans)
