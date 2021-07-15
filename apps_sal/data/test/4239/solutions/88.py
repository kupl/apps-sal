N = int(input())
ans = 100000
for A in range(N+1):
    num = 0
    B = N-A
    while A != 0:
        num  += A % 6
        A = A//6
    while B != 0:
        num  += B % 9
        B = B//9
    ans = min(ans,num)
print(ans)
