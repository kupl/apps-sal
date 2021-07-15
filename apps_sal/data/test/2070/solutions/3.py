A = list(map(int, input().split()))
L = [ord(i)-ord('a') for i in input()]

score = ans = 0
D = [dict() for i in range(26)]
for i in L :
    if score in D[i] :
        ans += D[i][score]
    score += A[i]
    if score not in D[i] :
        D[i][score] = 1
    else :
        D[i][score] += 1

print(ans)

