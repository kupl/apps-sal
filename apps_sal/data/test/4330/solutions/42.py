A, B = list(map(int, input().split()))
if A > B:
    A, B = B, A
diff = B - A
if diff % 2:
    print("IMPOSSIBLE")
else:
    print((A + diff // 2))


