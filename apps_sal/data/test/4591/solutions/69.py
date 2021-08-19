(A, B, C, X, Y) = map(int, input().split())
dif = abs(X - Y)
rem = max(X, Y)
if rem == X:
    E = A
else:
    E = B
com = rem - dif
ans = 0
D = A + B
if D < C * 2:
    ans += D * com
else:
    ans += C * com * 2
if E < C * 2:
    ans += E * dif
else:
    ans += C * dif * 2
print(ans)
