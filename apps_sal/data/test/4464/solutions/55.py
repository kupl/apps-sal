(A, B, C) = map(int, input().split())
dp = [0] * 1000
ans = 'NO'
cur_A = A
while 1:
    if cur_A % B == C:
        ans = 'YES'
        break
    elif dp[cur_A % B] == 1:
        ans = 'NO'
        break
    dp[cur_A % B] = 1
    cur_A += A
print(ans)
