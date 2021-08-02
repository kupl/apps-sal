N = int(input())
As = list(map(int, input().split()))

ans_step_sum = 0
current_max_height = As[0]

for Ai in As[1:]:
    diff = current_max_height - Ai
    if diff > 0: ans_step_sum += diff
    else: current_max_height = Ai
print(ans_step_sum)
