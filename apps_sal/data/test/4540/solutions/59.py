n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
a.append(0)


def cumulative_sum(collection):
    result = [0]
    for i in range(1, len(collection)):
        item = abs(collection[i] - collection[i - 1])
        result.append(result[-1] + item)
    return result


cuma = cumulative_sum(a)
lp = cuma[-1]
for i in range(n):
    gap = abs(cuma[i + 2] - cuma[i]) - abs(a[i + 2] - a[i])
    print(lp - gap, flush=True)
