n = int(input())
A = list(map(int, input().split()))
B = list(set(A))
if len(B) > 3:
    print(-1)
elif len(B) == 3:
    B.sort()
    if B[1] - B[0] == B[2] - B[1]:
        print(B[1] - B[0])
    else:
        print(-1)
elif len(B) == 1:
    print(0)
else:
    B.sort()
    if (B[1] - B[0]) % 2 == 0:
        print((B[1] - B[0]) // 2)
    else:
        print(B[1] - B[0])
