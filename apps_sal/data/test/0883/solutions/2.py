n = int(input())
s = input().split()
for i in range(n):
    s[i] = int(s[i])
t = sum(s)

ans = 5
for i in range(1, 6):
    x = t + i
    if(x % (n + 1) == 1):
        ans -= 1
print(ans)
