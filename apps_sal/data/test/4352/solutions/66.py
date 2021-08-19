(a, b) = map(int, input().split())
if a == 1:
    a = 14
if b == 1:
    b = 14
if a > b:
    ans = 'Alice'
elif a < b:
    ans = 'Bob'
else:
    ans = 'Draw'
print(ans)
