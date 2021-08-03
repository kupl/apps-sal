N = int(input())
P = list(map(int, input().split()))

mini = 2 * 10**5
ans = 0
for i in P:
    if i <= mini:
        ans += 1
        mini = i
print(ans)
