A = list(map(int, input().split()))

A.sort()
a_max = A[2]
a_middle = A[1]
a_min = A[0]
ans = 0

if sum(A) % 2 != (3 * a_max) % 2:  # 偶奇が等しいならば
    ans += 1
    a_max += 1
    a_middle += 1

ans += a_max - a_middle
ans += (a_max - (a_min + (a_max - a_middle))) // 2

print(ans)
