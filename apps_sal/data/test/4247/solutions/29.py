n = int(input())
li = list(map(int, input().split()))
cnt = 0
for i in range(1, n - 1):
    if li[i - 1] < li[i] and li[i] < li[i + 1]:
        cnt += 1
    elif li[i - 1] > li[i] and li[i] > li[i + 1]:
        cnt += 1

print(cnt)
