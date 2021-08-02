n = int(input())
a = list(map(int, input().split()))
ans = True
for i in range(0, n):
    if a[i] % 2 != 0:
        continue
    if a[i] % 3 == 0 or a[i] % 5 == 0:
        continue
    ans = False

if ans:
    print("APPROVED")
else:
    print("DENIED")
