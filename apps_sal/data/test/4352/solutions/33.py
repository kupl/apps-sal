A, B = map(int, input().split())
if A == 1:
    A = 14
if B == 1:
    B = 14
ans = 'Alice' if A > B else ('Bob' if A < B else 'Draw')
print(ans)
