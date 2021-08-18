N = int(input())
A = [int(x) for x in input().split()]
bucket = dict()
for i, num in enumerate(A):
    if num in bucket:
        bucket[num].append(i)
    else:
        bucket[num] = [i]
sorted_buckets = sorted((-len(val), val[-1] - val[0], val) for _, val in list(bucket.items()))
print(sorted_buckets[0][2][0] + 1, sorted_buckets[0][2][-1] + 1)
