N = int(input())
A = list(map(int,input().split()))
ans = 10**9
for x in A:
    if x % 2 == 1:
        print(0)
        return
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    ans = min(ans, c)
print(ans)
