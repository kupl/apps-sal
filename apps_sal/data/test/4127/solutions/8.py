A, B = input().split()
A = int(A)
i, d = list(map(int, B.split(".")))
B_m = i * 100 + d
ans = A * B_m // 100
print(ans)

