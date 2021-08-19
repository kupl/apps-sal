N = int(input())
A = [int(x) for x in input().split()]
bucket = dict()
for (i, num) in enumerate(A):
    if num in bucket:
        bucket[num].append(i)
    else:
        bucket[num] = [i]
sorted_buckets = sorted(list(bucket.values()), key=lambda val: (-len(val), val[-1] - val[0]))
print(sorted_buckets[0][0] + 1, sorted_buckets[0][-1] + 1)
