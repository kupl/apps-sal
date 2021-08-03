n = int(input())
tasks = [int(i) for i in input().split()]
max_seq = [1] * n
for i in range(n - 1):
    if tasks[i + 1] <= tasks[i] * 2:
        max_seq[i + 1] += max_seq[i]
print(max(max_seq))
