n = int(input())
a = list(map(int, input().split()))
t = int(input())
a.sort()
ans = 0
for i in range(n):
    j = i
    count = 0
    while j < n:
        if a[j] - a[i] <= t:
            count += 1
            j += 1
        else:
            break
    if count > ans:
        ans = count
print(ans)
