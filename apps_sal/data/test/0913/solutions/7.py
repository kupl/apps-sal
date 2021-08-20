n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = 0
b1 = 0
for i in range(n):
    if a[i] == 0 and b[i] == 1:
        b1 += 1
    elif a[i] == 1 and b[i] == 0:
        a1 += 1
if a1 == 0:
    print(-1)
elif a1 > b1:
    print(1)
elif a1 == b1:
    print(2)
else:
    print(b1 // a1 + 1)
