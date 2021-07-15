A, B = list(map(int, input().split()))
if A > B: A, B = B, A
if (B - A) & 1:
    print('IMPOSSIBLE')
    return
print((A + (B - A) // 2))

