taste = list(map(int, input().split()))
ans = 'No'

for i in range(2**4):
    tmp = sum(taste)
    res = 0
    for j in range(4):
        if i >> j & 1:
            res += taste[j]
            tmp -= taste[j]
    if tmp == res:
        ans = 'Yes'
        break

print(ans)
