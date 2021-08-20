N = int(input())
a = 0
for i in range(N):
    (Di1, Di2) = input().split()
    if Di1 == Di2:
        a = a + 1
        if a == 3:
            break
        else:
            a = a
    else:
        a = 0
if a >= 3:
    print('Yes')
else:
    print('No')
