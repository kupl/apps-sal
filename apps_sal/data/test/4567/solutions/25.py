N = int(input())
score = [int(input()) for _ in range(N)]
s_score = sorted(score)
a = 0
for i in s_score:
    if i % 10 != 0:
        a = i
        break
if sum(score) % 10 != 0:
    print(sum(score))
else:
    if a == 0:
        print(0)
    else:
        print(sum(score)-a)
