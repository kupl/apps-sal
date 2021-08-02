with open(0) as f:
    X, A, B = map(int, f.read().split())
if B - A <= 0:
    ans = 'delicious'
if 0 < B - A <= X:
    ans = 'safe'
if B - A > X:
    ans = 'dangerous'
print(ans)
