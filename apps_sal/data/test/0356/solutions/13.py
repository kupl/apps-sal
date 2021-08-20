n = int(input())
arr = [int(i) for i in input().split()]
m = int(input())
ar = [int(i) for i in input().split()]
a = arr[0]
b = ar[0]
aa = 1
bb = 1
ans = 0
while aa != n and bb != m:
    if a == b:
        a += arr[aa]
        aa += 1
        ans += 1
        continue
    if a < b:
        a += arr[aa]
        aa += 1
    else:
        b += ar[bb]
        bb += 1
while aa != n:
    a += arr[aa]
    aa += 1
while bb != m:
    b += ar[bb]
    bb += 1
if a == b:
    print(ans + 1)
else:
    print(-1)
