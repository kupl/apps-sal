n = int(input())
list_d = [int(i) for i in input().split()]
ans = 0
for i in range(0, n - 1):
    ans += list_d[i] * sum(list_d[i + 1:])
print(ans)
