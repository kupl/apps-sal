(A, B, C) = sorted(map(int, input().split()))
C -= A
B -= A
ans = 0
ans += C % 2
C -= C % 2
ans += B % 2
B -= B % 2
ans += 2 * (C // 2)
ans -= B // 2
print(ans)
