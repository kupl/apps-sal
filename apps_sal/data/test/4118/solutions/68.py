A, B = map(int, input().split())

# A, Bがともに9以下であるかどうかで場合分け
if A <= 9 and B <= 9:
    print(A * B)
else:
    print(-1)
