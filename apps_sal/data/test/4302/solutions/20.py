A, B = map(int, input().split())
ans = max(A + A - 1, B + B - 1, A + B)
print(ans)
