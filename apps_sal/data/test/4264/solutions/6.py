N = int(input())
ans = 0
for i in range(1, N + 1):
    num = len(str(i))
    if num % 2 != 0:
        ans += 1
print(ans)
