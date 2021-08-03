A, B, X = list(map(int, input().split()))
if A <= X and X <= A + B:
    print("YES")
else:
    print("NO")
