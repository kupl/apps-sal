from random import randint
from time import time
n = list(map(int, input().strip().split()))[0]
arr = list(map(int, input().strip().split()))
tik = time()
count = dict()
subsum = [0 for i in range(n + 1)]
for index in range(len(arr) - 1, -1, -1):
    if arr[index] in count:
        count[arr[index]] += 1
    else:
        count[arr[index]] = 1
    if index == len(arr) - 1:
        subsum[index] = arr[index]
    else:
        subsum[index] = arr[index] + subsum[index + 1]
answer = 0
for (index, value) in enumerate(arr):
    answer += subsum[index + 1] - (len(arr) - index - 1) * arr[index]
    if value + 1 in count:
        answer -= count[value + 1]
    if value - 1 in count:
        answer += count[value - 1]
    count[value] -= 1
    if count[value] == 0:
        count.pop(value)
print(answer)
