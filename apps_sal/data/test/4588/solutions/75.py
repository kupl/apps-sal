(X, Y) = map(str, input().split())
if X < Y:
    ans = '<'
elif X > Y:
    ans = '>'
else:
    ans = '='
print(ans)
