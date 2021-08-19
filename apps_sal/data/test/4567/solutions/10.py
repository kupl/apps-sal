# 16 C - Bugged
N = int(input())
s = [int(input()) for _ in range(N)]
s = sorted(s, reverse=False)

score = sum(s)
if score % 10 == 0:
    for i in s:
        score -= i
        if score % 10 != 0:
            break
        score += i
    else:
        score = 0
print(score)
