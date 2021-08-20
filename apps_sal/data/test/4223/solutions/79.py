n = int(input())
c = input()
ans = 1
for i in range(1, n):
    if c[i] != c[i - 1]:
        ans += 1
print(ans)
