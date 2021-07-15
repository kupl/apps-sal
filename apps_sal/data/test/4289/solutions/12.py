_, ta, hs = int(input()), list(map(int, input().split())), list(map(int, input().split()))
t, a = ta[0], ta[1]
min_diff, answer = float('inf'), 0
for index, h in enumerate(hs):
    diff = abs(a - (t - h * 0.006))
    if diff <= min_diff:
        min_diff, answer = diff, index + 1

print(answer)

