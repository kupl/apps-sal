# C
# A*B+C=N A*B=N-C
n = int(input())
ans = 0
for i in range(1, n):
    ans += (n - 1) // i
print(ans)
