a, b, c = map(int, input().split())

lis = [a, b, c]
lis.sort(reverse=True)
maxi = lis[0]
mid = lis[1]
mini = lis[2]
cnt = 0


while maxi > mid:
    cnt += 1
    mini += 1
    mid += 1

if (maxi - mini) % 2 == 0:
    cnt += (maxi - mini) // 2
else:
    cnt += (maxi - mini + 1) // 2 + 1

print(cnt)
