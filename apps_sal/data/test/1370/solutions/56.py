from itertools import product
h, w, k = list(map(int, input().split()))
arr = [[int(i) for i in input()] for _ in range(h)]

ans = 2000

for cond in product([True, False], repeat=(h - 1)):
    cut = sum(cond)
    div = 0
    splits = [0] * (cut + 1)
    splits[0] = arr[0][:]
    for i in range(1, h):
        if cond[i - 1]:
            div += 1
            splits[div] = arr[i][:]
        else:
            splits[div] = [splits[div][j] + arr[i][j] for j in range(w)]

    check = [max(i) for i in splits]
    if max(check) > k:
        break
    count = [i[0] for i in splits]

    for j in range(1, w):
        addarr = [count[i] + splits[i][j] for i in range(cut + 1)]
        if max(addarr) > k:
            div += 1
            count = [splits[i][j] for i in range(cut + 1)]
        else:
            count = addarr[:]
    ans = min(ans, div)

print(ans)
