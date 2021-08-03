A, B = map(int, input().split())
ans = (B - A + (B % 2) - (A % 2)) // 2 % 2 ^ (A * (A % 2)) ^ (B * (B % 2 < 1))
print(ans)
