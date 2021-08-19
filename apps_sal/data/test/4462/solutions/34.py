N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    if a[i] % 4 == 0:
        a[i] = 2
    elif a[i] % 2 == 0:
        a[i] = 1
    else:
        a[i] = 0
zero = a.count(0)
one = a.count(1)
two = a.count(2)
if zero > two + 1:
    print('No')
elif zero == two + 1:
    if zero + two == N:
        print('Yes')
    else:
        print('No')
else:
    print('Yes')
