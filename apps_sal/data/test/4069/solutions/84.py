#n = int(input())
x, k, d = list(map(int, input().split()))
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
x = abs(x)
if x//d >= k:
    ans = x-d*k
else:
    mnmove = x//d
    k -= mnmove
    x -= mnmove*d
    if k % 2 == 0:
        ans = x
    else:
        ans = abs(x-d)

print(ans)

