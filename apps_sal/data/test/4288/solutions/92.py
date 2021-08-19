(A, B, C) = map(int, input().split())
ans = 0
if A == B:
    ans += 1
if B == C:
    ans += 1
if A == C:
    ans += 1
if ans == 1:
    print('Yes')
else:
    print('No')
