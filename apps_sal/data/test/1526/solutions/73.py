(A, B, C) = sorted(map(int, input().split()))
ans = (C - A) // 2 + (C - B) // 2
A += 2 * ((C - A) // 2)
B += 2 * ((C - B) // 2)
if A == B:
    if A < C:
        ans += 1
else:
    ans += 2
print(ans)
