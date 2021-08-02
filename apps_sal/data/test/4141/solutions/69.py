n = int(input())
a = list(map(int, input().split()))
count = 0
total = 0
for i in range(n):
    if a[i] % 2 == 0:
        count += 1
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            total += 1
if count == total:
    print("APPROVED")
else:
    print("DENIED")
