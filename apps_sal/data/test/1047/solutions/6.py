k = [int(i) for i in input()]
print(max(k))
nums = []
while max(k) > 0:
    d = ['0'] * len(k)
    for x in range(len(k)):
        if k[x] > 0:
            k[x] -= 1
            d[x] = '1'
    n = ''.join(d)
    while n[0] == '0':
        n = n[1:]
    nums.append(n)
print(' '.join(nums))
