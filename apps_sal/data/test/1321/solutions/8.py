n = int(input())
friends = [tuple(map(int, input().split())) for _ in range(n)]
w_sum = sum((friend[0] for friend in friends))
(top_height_0, top_height_1) = sorted((friend[1] for friend in friends), reverse=True)[:2]
for friend in friends:
    print((w_sum - friend[0]) * (top_height_0 if friend[1] != top_height_0 else top_height_1), end=' ')
