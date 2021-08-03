

n, x = list(map(int, input().split()))
l = list(map(int, input().split()))

l1 = [0] + l
for i in range(1, len(l) + 1):
    l1[i] = l1[i - 1] + l[i - 1]
cnt = 0

for i in range(0, len(l1)):
    if (l1[i] <= x):
        cnt += 1
print(cnt)
