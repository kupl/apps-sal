(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
last_score = sum(a)
score = n * m - last_score
if score <= k:
    if score > 0:
        print(score)
    else:
        print(0)
else:
    print(-1)
