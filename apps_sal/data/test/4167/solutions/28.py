n, k = map(int, input().split())
ans = 0

if k%2 == 1:
    ans = (n//k)**3
else:
    ans = (n//k)**3 + ((n + k//2)//k)**3

print(ans)
