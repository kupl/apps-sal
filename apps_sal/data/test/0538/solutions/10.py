n = int(input())
while (n % 10 == 0):
    n //= 10
n = str(n)
ans = "YES"
for i in range(len(n) // 2 + 1):
    if (n[i] != n[len(n) - i - 1]):
        ans = "NO"
print(ans)
