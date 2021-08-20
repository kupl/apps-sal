(A, B) = list(map(int, input().split()))
ans = A - B * 2
if ans <= 0:
    print(0)
else:
    print(ans)
