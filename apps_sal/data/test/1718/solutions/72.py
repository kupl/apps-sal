n,k = list(map(int,input().split()))
A = list(map(int,input().split()))

key = 2*k - 2

if key >n:
    if k == n:
        ans = 1
    else:
        ans = 2

elif n % key == 0:
    ans = 2*(n // key)

else:
    if n % key == 1:
        ans = 2*(n // key)
    elif (n % key) + 1 > k:
        ans = 2*(n // key) + 2
    else:
        ans = 2*(n // key) + 1

print(ans)

