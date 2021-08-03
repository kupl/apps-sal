N = int(input())
d4 = 0
d2 = 0
for i in list(map(int, input().split())):
    if i % 4 == 0:
        d4 += 1
    elif i % 2 == 0:
        d2 += 1
    else:
        None
if N <= d4 * 2 + 1:
    print("Yes")
elif N - d4 * 2 <= d2:
    print("Yes")
else:
    print("No")
