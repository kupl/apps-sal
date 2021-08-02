n = int(input())
a = [int(i) for i in input().split()]

ans = 0
for num in a:
    tmp = min(num - 1, 10**6 - num)
    ans = max(ans, tmp)
print(ans)
