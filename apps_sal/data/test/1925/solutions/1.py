A, B, N = [int(_) for _ in input().split()]

i = min(N, B-1)
ans = (A * i) // B - A * (i // B)

print(ans)

