import numpy as np
(X, K, D) = map(int, input().split())
ans = 0
if X >= 0:
    if int(X / D) <= K:
        if int(X / D) % 2 == K % 2:
            ans = X % D
        else:
            ans = D - X % D
    else:
        ans = abs(X - K * D)
if X < 0:
    if abs(int(X / D)) <= K:
        if abs(int(X / D)) % 2 == K % 2:
            ans = abs(X) % D
        else:
            ans = D - abs(X) % D
    else:
        ans = abs(X + K * D)
print(ans)
