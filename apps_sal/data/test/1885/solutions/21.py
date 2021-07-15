def fact(a):
    ans = 1
    for i in range(2, a + 1):
        ans *= i
    return ans

n = int(input())
ans = 0
for i in range(5, 8):
    ans += fact(n) // fact(i) // fact(n - i)
print(ans)
