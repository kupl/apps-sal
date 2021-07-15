n = int(input())
a = list(map(int, input().split()))
curr = 1
maxx = 1
for i in range(n - 1):
    if a[i] * 2 < a[i + 1]:
        maxx = max(maxx, curr)
        curr = 1
    else:
        curr += 1
maxx = max(curr, maxx)
print(maxx)
