n, k = map(int, input().split())
j = 0
m = 0
ans = 0
if k % 2 == 1:
    j = n // k
    # print('j',j)
    ans = j * j * j

else:
    j = n // k
    m = (n - k // 2) // k + 1
    # print('j',j,'m',m)
    ans = m * m * m + j * j * j

print(ans)
