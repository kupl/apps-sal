(A, B) = map(int, input().split())
if A > B:
    if (A - B) % 2 == 0:
        print(B + (A - B) // 2)
    else:
        print('IMPOSSIBLE')
elif (B - A) % 2 == 0:
    print(A + (B - A) // 2)
else:
    print('IMPOSSIBLE')
