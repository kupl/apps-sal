n = int(input())
inf = False
A = list(map(int, input().split()))
for i in range(1, n):
    if (A[i] == 2 and A[i - 1] == 3) or (A[i] == 3 and A[i - 1] == 2):
        inf = True
if inf:
    print('Infinite')
else:
    print('Finite')
    ans = 0
    for i in range(1, n):
        a = A[i - 1]
        b = A[i]
        if a > b:
            a, b = b, a
        if a == 1 and b == 2:
            ans += 3
        elif a == 1 and b == 3:
            ans += 4
        if i > 1 and A[i] == 2 and A[i - 2] == 3:
            ans -= 1
    print(ans)
