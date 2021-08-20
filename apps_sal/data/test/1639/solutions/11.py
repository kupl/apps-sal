n = int(input())
A = list(map(int, input().split()))
count = 0
ans = 0
prev = -1
for a in A:
    if prev <= a:
        count += 1
        ans = max(ans, count)
    else:
        count = 1
    prev = a
print(ans)
