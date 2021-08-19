(x, a, b) = list(map(int, input().split()))
if a >= b:
    ans = 'delicious'
elif a + x >= b:
    ans = 'safe'
else:
    ans = 'dangerous'
print(ans)
