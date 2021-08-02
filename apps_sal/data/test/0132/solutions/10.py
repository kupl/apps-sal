n = int(input())
slices = list(map(int, input().split()))
answer = 360
for i in range(n):
    for j in range(i + 1, n):
        cur_s = abs(sum(slices[:i]) + sum(slices[j:]) - sum(slices[i:j]))
        answer = min(cur_s, answer)
print(answer)
