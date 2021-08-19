(A, B, C) = map(int, input().split())
if C - (A - B) < 0:
    print(0)
else:
    print(C - (A - B))
