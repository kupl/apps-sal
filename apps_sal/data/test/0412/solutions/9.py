n = int(input())
arr = list(map(int, input().split()))
ans = [0 for i in range(n)]
j = 2
for i in range(n):
    while arr[i] % j == 0:
        ans[i] += 1
        arr[i] //= j
print(2 ** max(ans), ans.count(max(ans)))

