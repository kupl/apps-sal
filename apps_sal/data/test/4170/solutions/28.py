n = int(input())
h = list(map(int, input().split()))
count = 0
max_move = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        count += 1
        if count > max_move:
            max_move = count
    else:
        count = 0
print(max_move)
