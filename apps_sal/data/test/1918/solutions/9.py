def cnt(step):
    (temp_total, ans) = (total, 0)
    for i in range(N)[::step]:
        if chars[i] == 'A':
            temp_total += strengths[i]
        else:
            temp_total -= strengths[i]
        ans = max(temp_total, ans)
    return ans


N = int(input())
strengths = [int(_) for _ in input().split()]
chars = list(input())
total = 0
for (i, c) in enumerate(chars):
    if c == 'B':
        total += strengths[i]
print(max([total, cnt(1), cnt(-1)]))
