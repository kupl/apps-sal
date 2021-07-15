n, k, m = map(int, input().split())
a = (map(int, input().split()))

sum_Score = sum(a)
good = ((m * n) - (sum_Score))

if good > k:
    print('-1')
else:
    print(max(good, 0))
