n = int(input())
a = list(map(int, input().split()))
ans = 0
neg = 0
zero = False
smallest = abs(a[0])
for i in range(n):
    ans += abs(a[i])
    if abs(a[i]) < smallest:
        smallest = abs(a[i])
    if a[i] == 0:
        zero = True
    elif a[i] < 0:
        neg += 1
if neg % 2 == 1 and (not zero):
    print(ans - 2 * smallest)
else:
    print(ans)
