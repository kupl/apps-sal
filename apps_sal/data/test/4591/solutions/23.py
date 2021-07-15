
A,B,C,X,Y = list(map(int, input().split()))

ans1 = (2*C)*min(X,Y) + A*(X-min(X,Y)) + B*(Y-min(X,Y))
ans2 = A*X + B*Y
ans3 = 2*C*max(X,Y)

ans = min(ans1,ans2,ans3)
print(ans)


