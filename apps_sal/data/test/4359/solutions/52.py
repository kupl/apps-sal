import itertools

arr = []
mins = []

for _ in range(5):
    arr.append(int(input()))

for comb in list(itertools.permutations(arr)):
    ans = 0
    for (i, ele) in enumerate(comb):
        ans += ele
        if not i == len(comb) - 1:
            diff = 10 - (ans % 10)
            if diff == 10:
                diff = 0
            ans += diff
    mins.append(ans)

print(min(mins))
