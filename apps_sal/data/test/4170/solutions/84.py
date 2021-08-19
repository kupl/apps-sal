N = int(input())
H = list(map(int, input().split()))
moves = [H[i + 1] - H[i] for i in range(0, len(H) - 1)]
max_move = 0
count = 0
for (i, m) in enumerate(moves):
    if m <= 0:
        count += 1
    else:
        max_move = max(count, max_move)
        count = 0
max_move = max(max_move, count)
print(max_move)
