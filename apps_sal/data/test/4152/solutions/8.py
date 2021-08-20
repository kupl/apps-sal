import bisect
n = int(input())
nums = list(map(int, input().split()))
pows = [pow(2, x) for x in range(31)]
dict = {}
for num in nums:
    if num not in dict:
        dict[num] = 1
    else:
        dict[num] += 1
count = 0
for (k, v) in dict.items():
    count += v
    for i in range(bisect.bisect_right(pows, k), 31):
        if pows[i] - k in dict:
            if pows[i] == 2 * k and v == 1:
                continue
            count -= v
            break
print(count)
