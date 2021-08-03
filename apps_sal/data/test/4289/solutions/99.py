N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

tmp = float("inf")
ans = 0

for i in range(N):
    num = abs(A - (T - H[i] * 0.006))
    if tmp > num:
        ans = i + 1
        tmp = num

print(ans)
