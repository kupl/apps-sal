(n, m) = map(int, input().split())
l = list(map(int, input().split()))
count = 0
sum = 0
i = 0
while i < n:
    sum = sum + l[i]
    if sum == m:
        sum = 0
        count = count + 1
        i = i + 1
    elif sum > m:
        sum = 0
        count = count + 1
    else:
        i = i + 1
if sum < m and sum > 0:
    count = count + 1
    i = i + 1
print(count)
