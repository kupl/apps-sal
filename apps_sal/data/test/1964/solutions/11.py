n = int(input())
c = list(map(int, input().strip().split()))
ans = 1 << 31
for i in range(n):
    ans = min(ans, sum([int(k) * 5 for k in input().split()]) + c[i] * 15)
print(ans)
