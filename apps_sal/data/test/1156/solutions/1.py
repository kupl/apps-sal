n = int(input())
a = list(map(int, input().split()))
b = input()
l = -(10**9)
r = 10**9
for i in range(4, n):
    if b[i] == '1' and b[i-4:i] == '0000':
        l = max(l, max([a[i],a[i-1], a[i-2], a[i-3], a[i-4]])+1)
    elif b[i] == '0' and b[i-4:i] == '1111':
        r = min(r, min([a[i],a[i-1], a[i-2], a[i-3], a[i-4]])-1)
print(l, r)
