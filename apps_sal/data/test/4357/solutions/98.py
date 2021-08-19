(A, B, C) = list(map(int, input().split()))
if A >= B and A >= C:
    print(int(A * 10 + B + C))
elif B >= A and B >= C:
    print(int(B * 10 + A + C))
else:
    print(int(C * 10 + A + B))
