A = list(map(int, input().split()))
S = [ord(x) - ord('a') for x in input()]
score = ans = 0
D = [dict() for _ in range(26)]
for i in S:
    if score in D[i]:
        ans += D[i][score]
    score += A[i]
    if score in D[i]:
        D[i][score] += 1
    else:
        D[i][score] = 1
print(ans)
