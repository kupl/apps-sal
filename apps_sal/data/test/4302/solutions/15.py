A, B = map(int, input().split())
if abs(A - B) == 0:
    ans = A + B
elif abs(A - B) == 1:
    ans = max(A, B) + min(A, B)
else:
    ans = max(A, B) + max(A, B) - 1
print(ans)
