from math import ceil
t = 1
for test in range(t):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    index = 0
    for i in a:
        if index >= m:
            break
        if b[index] >= i:
            ans += 1
            index += 1
    print(ans)
