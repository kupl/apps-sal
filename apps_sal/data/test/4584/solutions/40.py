n = int(input())
ans = [0] * n
a = list(map(int, input().split()))
for i in range(n - 1):
    ans[a[i] - 1] += 1
print(*ans, sep='\n')
