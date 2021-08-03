A, B = map(int, input().split())
if(A <= 9 and A >= 1 and B <= 9 and B >= 1):
    print(int(A * B))
else:
    print(-1)
