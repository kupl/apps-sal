n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt += arr[i] % 2
print(min(cnt, n - cnt))
