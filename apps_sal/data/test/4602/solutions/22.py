n = int(input())
k = int(input())
x = [int(x) for x in input().split()]


ans = 0
for i in range(n):
    ans += 2*min(x[i], abs(x[i]-k))

print(ans)
