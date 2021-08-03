N = int(input())
A = 1
ans = [-1 for i in range(2)]
while 3 ** A <= N:
    B = 1
    while 3 ** A + 5 ** B <= N:
        if 3 ** A + 5 ** B == N:
            ans[0] = A
            ans[1] = B
            break
        B += 1
    A += 1

if ans[0] < 0:
    print(-1)
else:
    print(ans[0], ans[1])
