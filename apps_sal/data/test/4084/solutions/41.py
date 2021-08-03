n, a, b = list(map(int, input().split()))
cnt = n // (a + b)
rem = n - cnt * (a + b)
ans = cnt * a
if(rem > a):
    ans += a
else:
    ans += rem
print(ans)
