n = int(input())
a = list(map(int, input().split()))
mx = 0
ct = 0
for i in range(n - 2):
    if a[i] + a[i + 1] == a[i + 2]:
        ct += 1
        if ct > mx:
            mx = ct
    else:
        ct = 0
if n <= 2:
    print(n)
else:
    print(mx + 2)
