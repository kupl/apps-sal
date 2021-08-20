(A, B, C) = list(map(int, input().split()))
ans = C - A + B
if ans <= 0:
    print(0)
else:
    print(ans)
