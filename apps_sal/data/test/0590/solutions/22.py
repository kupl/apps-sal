from collections import Counter

n = int(input())

arr = [int(x) for x in input().split(" ")]
counter = Counter(arr)


s = {x for x in range(1, n + 1)}
replacements = sorted(list(s - set(counter.keys())))

r = 0
ans = 0
skipped = set()
for index, value in enumerate(arr):
    if counter[value] > 1:
        if value > replacements[r] or value in skipped:
            arr[index] = replacements[r]
            ans += 1
            r += 1
            counter.subtract((value,))
        else:
            skipped.add(value)


print(ans)
print(" ".join([str(x) for x in arr]))
