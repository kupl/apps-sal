import itertools
array = list(map(int, input().split()))
ans = 'No'
for i in range(4):
    for tmp in itertools.combinations(array, i + 1):
        if sum(tmp) * 2 == sum(array):
            ans = 'Yes'
print(ans)
