(A, B) = map(int, input().split())
if A < B:
    if A == 1:
        ans = 'Alice'
    else:
        ans = 'Bob'
elif B < A:
    if B == 1:
        ans = 'Bob'
    else:
        ans = 'Alice'
else:
    ans = 'Draw'
print(ans)
