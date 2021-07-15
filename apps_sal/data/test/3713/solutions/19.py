n = int(input())
s = input()
arr = list(map(int, s))
cnt = 0
pcnt = 0
for i in range(n - 1):
    cnt += arr[i] != arr[i + 1]
    pcnt += arr[i] == arr[i + 1]
cnt += min(pcnt, 2)
print(cnt + 1)
