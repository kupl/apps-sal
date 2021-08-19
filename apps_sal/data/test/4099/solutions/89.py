(n, k, m) = map(int, input().split())
total = sum(list(map(int, input().split())))
lowest_score = m * n
add_score = lowest_score - total
if add_score <= 0:
    print(0)
elif add_score > k:
    print(-1)
else:
    print(add_score)
