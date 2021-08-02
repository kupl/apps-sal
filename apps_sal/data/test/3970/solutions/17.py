n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
if k == 1:
    print(len(nums))
else:
    r = set()
    for i in sorted(nums):
        if i in r:
            continue
        else:
            r.add(i * k)
    print(len([i for i in nums if i not in r]))
