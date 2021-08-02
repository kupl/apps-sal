A, B = list(map(str, input().split()))
ans = int(A) * int(B[0]) * 100
ans += (int(A) * int(B[2]) * 10)
ans += (int(A) * int(B[3]))
print((ans // 100))
