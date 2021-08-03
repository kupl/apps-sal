n = int(input())
arr = list(map(int, input().strip().split(' ')))
arr.sort()
ind = n
cnt = 0
for i in range(n // 2 - 1, -1, -1):
    cnt = cnt + abs(arr[i] - ind)
    ind -= 2
cnt1 = 0
ind = n - 1
for i in range(n // 2 - 1, -1, -1):
    cnt1 = cnt1 + abs(arr[i] - ind)
    ind -= 2
print(min(cnt, cnt1))
