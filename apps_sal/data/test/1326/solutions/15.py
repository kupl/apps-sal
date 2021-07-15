N = int(input())
ans = 0
for i in range(1, N + 1):
    res = N // i
    ans += res*(res+1)//2*i
print(ans)
