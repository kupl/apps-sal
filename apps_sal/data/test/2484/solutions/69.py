N = int(input())
A = list(map(int, input().split()))
(xsum, sum) = (A[0], A[0])
(ans, x, y) = (0, 0, 0)
flag = True
while flag:
    if xsum == sum:
        ans += x - y + 1
        x += 1
        if x == N:
            break
        sum += A[x]
        xsum ^= A[x]
    else:
        sum -= A[y]
        xsum ^= A[y]
        y += 1
print(ans)
