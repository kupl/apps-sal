n = int(input())
A = list(map(int, input().split()))
left = [0 for _ in range(10 ** 5 + 1)]
right = [0 for _ in range(10 ** 5 + 1)]
r_non0 = 0
for a in A:
    if right[a] == 0:
        r_non0 += 1
    right[a] += 1
ans = 0
for i in range(n):
    left[A[i]] += 1
    right[A[i]] -= 1
    if right[A[i]] == 0:
        r_non0 -= 1
    if left[A[i]] == 1:
        ans += r_non0
print(ans)
