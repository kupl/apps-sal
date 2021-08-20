(X, A, B) = map(int, input().split())
date = A - B
if date >= 0:
    ans = 'delicious'
elif abs(date) > X:
    ans = 'dangerous'
else:
    ans = 'safe'
print(ans)
