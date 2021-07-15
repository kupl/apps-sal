s = input()
n = len(s)
ans = 0
for i in range(n):
    a = int(s[i])
    for j in range(n-i):
        ans += a * 10**j * 2**(max(0,n-i-j-2)) * 2**(i)
print(ans)
