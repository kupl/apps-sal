with open('input.txt') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
mark = [0 for _ in range(5001)]
sumMark = [0 for _ in range(5001)]
total = 0
minA = 1000000
for v in arr:
    mark[v] += 1
    total += 1
for i in range(1, 5001):
    if mark[i] > 0:
        sumMark[i] = sumMark[i - 1] + mark[i]
    else:
        sumMark[i] = sumMark[i - 1]
for i in range(1, 5001):
    if i <= 2500:
        if mark[i] > 0:
            preValue = sumMark[i - 1]
            postValue = total - sumMark[i * 2]
            remove = postValue + preValue
            ret = total - remove
            if remove < minA:
                minA = remove
    elif mark[i] > 0:
        remove = sumMark[i - 1]
        ret = total - remove
        if remove < minA:
            minA = remove
with open('output.txt', 'w') as f:
    f.write(str(minA))
