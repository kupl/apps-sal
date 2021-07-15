def binary_search(key):
    bad, good = -1, len(ans)
    while good - bad > 1:
        mid = (bad + good) // 2
        if ans[mid][-1] < key:
            good = mid
        else:
            bad = mid
    return good


N = int(input())
ans = []
for _ in range(N):
    A = int(input())
    idx = binary_search(A)
    if idx == len(ans):
        ans.append([A])
    else:
        ans[idx].append(A)
print((len(ans)))

