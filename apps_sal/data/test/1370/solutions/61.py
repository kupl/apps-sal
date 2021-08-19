from itertools import product
(h, w, k) = list(map(int, input().split()))
arr = [[int(i) for i in input()] for _ in range(h)]
ans = 2000
for cond in product([True, False], repeat=h - 1):
    cut = sum(cond)
    splits = [arr[0][:]]
    for i in range(1, h):
        if cond[i - 1]:
            splits.append(arr[i][:])
        else:
            splits[-1] = [splits[-1][j] + arr[i][j] for j in range(w)]
    check = [max(i) for i in splits]
    if max(check) > k:
        break
    count = [i[0] for i in splits]
    div = cut
    for j in range(1, w):
        addarr = [count[i] + splits[i][j] for i in range(cut + 1)]
        if max(addarr) > k:
            div += 1
            count = [splits[i][j] for i in range(cut + 1)]
        else:
            count = addarr[:]
    ans = min(ans, div)
print(ans)
