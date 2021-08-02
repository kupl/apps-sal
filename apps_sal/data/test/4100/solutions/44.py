n, k, q = map(int, input().split())
A = [int(input()) for _ in range(q)]
score = [k - q] * n
for a in A:
    score[a - 1] += 1
for i in range(n):
    print("Yes" if score[i] > 0 else "No")
