from collections import Counter
A = list(map(int, input().split()))
L = [ord(i) - ord('a') for i in input()]

score = ans = 0
D = [Counter() for i in range(26)]
for i in L:
    ans += D[i][score]
    score += A[i]
    D[i][score] += 1

print(ans)
