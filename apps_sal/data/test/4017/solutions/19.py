import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

count = {}

sum = 0
for i in range(n):
    if a[i] not in count.keys():
        count[a[i]] = 0
    count[a[i]] += 1

    sum += a[i]

ans = []

for i in range(n):
    sub = sum - a[i]
    if sub % 2 == 1:
        continue
    sub = int(sub/2)
    if sub in count.keys() and sub == a[i]:
        if count[sub] > 1:
            ans.append(str(i+1))
    elif sub in count.keys() and count[sub] >= 1:
        ans.append(str(i+1))

print(len(ans))
print(" ".join(ans))
