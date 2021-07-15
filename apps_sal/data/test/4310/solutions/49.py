A1, A2, A3 = map(int, input().split())
ans = max(A1, A2, A3) - min(A1, A2, A3)

print(ans)
