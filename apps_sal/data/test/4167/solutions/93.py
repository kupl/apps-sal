n, k = map(int,input().split())
if k % 2:
    ans = (n // k)**3
else:
    ans = ((k//2 + n) // k)**3 + (n // k)**3
print(ans)
