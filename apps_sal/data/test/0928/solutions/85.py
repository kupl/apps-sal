n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
r = 0
sumi = 0
for i in range(0, len(a)):
    while(sumi < k):
        if (r == len(a)):
            break
        else:
            sumi += a[r]
            r += 1
    if sumi < k:
        break
    count += n - r + 1
    sumi -= a[i]
print(count)
