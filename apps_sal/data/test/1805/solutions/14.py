Q = int(input())
for q in range(Q):
    n = int(input())
    if n == 2:
        ans = 2
    elif n % 2 == 1:
        ans = 1
    else:
        ans = 0
    print(ans)
