def solve(curr, other, k):
    t = 0
    while t < k and t < len(curr) and (t < len(other)) and (other[t] > curr[t]):
        t += 1
    return t


(n, k) = map(int, input().split())
arr = list(map(int, input().split()))
maxx = -10 ** 100
for i in range(n):
    curr = []
    other = sorted(arr[:i] + arr[i + 1:], reverse=True)
    for j in range(i, n):
        curr.append(arr[j])
        curr.sort()
        if j < n - 1:
            del other[other.index(arr[j + 1])]
        t = min(len(curr), len(other), k)
        t = solve(curr, other, k)
        maxx = max(maxx, sum(curr) - sum(curr[:t]) + sum(other[:t]))
print(maxx)
