A, B, C = map(int, input().split())
if A == 5 and B == 5 and C == 7:
    print("YES")
elif A == 5 and C == 5 and B == 7:
    print("YES")
elif C == 5 and B == 5 and A == 7:
    print("YES")
else:
    print("NO")
