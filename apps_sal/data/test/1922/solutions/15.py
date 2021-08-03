n, m = map(int, input().split())
if(n == 1) & (m == 1):
    ans = 1
elif(n == 1) | (m == 1):
    ans = n + m - 3
else:
    ans = (n - 2) * (m - 2)
print(ans)
