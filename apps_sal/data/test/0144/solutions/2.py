n = int(input())
a = list(map(int, input().rstrip()))
sm = sum(a)
ans = False
for cnt in range(2, n + 1):
    if sm % cnt != 0:
        continue
    seq_sum = sm // cnt
    cur_sum = 0
    ans = True
    for i in range(n):
        cur_sum += a[i]
        if cur_sum == seq_sum:
            cur_sum = 0
        if cur_sum > seq_sum:
            ans = False
            break
    if ans:
        break
print('YES' if ans else 'NO')
