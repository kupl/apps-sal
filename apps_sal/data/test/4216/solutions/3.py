n = int(input())
i = 1
ans = float("inf")
while i**2 <= n:
    if n%i == 0:
        ans = min(ans, max(len(str(i)), len(str(n//i))))
    i += 1
print(ans)
