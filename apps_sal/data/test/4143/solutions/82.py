N = int(input())
move = []

for _ in range(5):
    move.append(int(input()))

min_value = min(move)
group_count = -(-N // min_value)

# 最後のグループが出発するまでの値はgroup_count - 1
print((group_count - 1 + 5))
