A, B, C =map(int, input().split())

if (A - B) < C:
    print(C - (A-B))
else:
    print(0)
