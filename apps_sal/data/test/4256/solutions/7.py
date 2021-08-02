A, B, C = map(int, input().split())
ans = int(B / A) if int(B / A) <= C else C
print(ans)
