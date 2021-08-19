(A, B) = map(int, input().split())
ans = A - 2 * B
if ans < 0:
    print(0)
else:
    print(ans)
