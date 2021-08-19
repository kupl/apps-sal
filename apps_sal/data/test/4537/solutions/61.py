(A, B) = map(int, input().split())
ans = max(A + B, A - B, A * B)
print(ans)
