n = int(input().strip())
arr = list(map(lambda x: int(x) - 1, input().strip().split()))

maximum = 0
answer = 0
for start, end in enumerate(arr):
    maximum = max(maximum, end)
    if maximum == start:
        answer += 1

print(answer)
