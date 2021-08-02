import sys

limit = 300

m, span, need = list(map(int, input().split()))
visits = list(map(int, input().split()))
if need > span:
    print(-1)
    return

result = 0
count = (limit + 1) * [0]
for visit in visits:
    for i in range(need - count[visit]):
        for pos in range(max(0, visit - i), min(visit - i + span, limit + 1)):
            count[pos] += 1
        result += 1
print(result)
