from itertools import product
A = list(map(int, input().split()))
x = sum(A)
ans = 'No'
for p in product(range(2), repeat=4):
    y = 0
    for (p_idx, p_) in enumerate(p):
        if p_ == 1:
            y += A[p_idx]
    if x - y == y:
        ans = 'Yes'
print(ans)
