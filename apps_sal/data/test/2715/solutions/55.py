k = int(input())

n = 50
a = k // n
m = k % n
ans = list(range(a, a + n))
for i in range(m):
    ans[n - i - 1] += 1

print(50)
print(*ans)
