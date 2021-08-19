(A, B) = map(int, input().split())
ans = [A + A - 1, A + B, B + B - 1]
print(max(ans))
