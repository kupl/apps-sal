aints = int(input())
nums = list(map(int, input().split(' ')))
compute = [0] * 100001
for i in nums:
    compute[i] += 1

answer = [0, compute[1]] + [-1] * (100000)

for i in range(2, 100001):
    answer[i] = max(compute[i] * i + answer[i - 2], answer[i - 1])
print(answer[-2])
