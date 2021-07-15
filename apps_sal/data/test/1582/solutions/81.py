from collections import defaultdict
N = int(input())

head_tail = defaultdict(int)
for i in range(1, N + 1):
    tail = i % 10
    head = int(str(i)[0])
    head_tail[(head, tail)] += 1

answer = 0
for i in range(1, N + 1):
    head = int(str(i)[0])
    tail = i % 10
    answer += head_tail[(tail, head)]
print(answer)
