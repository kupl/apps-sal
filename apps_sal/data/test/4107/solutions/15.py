n, k = (int(i) for i in input().split())
string = input()

INF = 10**100
cache = [INF] * n
def getVal(idx):
    if idx < 0 or cache[idx] == INF:
        return 0
    return cache[idx]

last_idx = 0
reached_end = False
for i in range(n):
    if string[i] == '0':
        new = getVal(i-1)+i+1
        cache[i] = min(cache[i], new)
    else:
        new = getVal(i-1-k)+i+1
        if new < cache[i]:
            cache[i] = new
            last_idx = 0

        if reached_end:
            continue
        end = i+k+1
        if end >= n:
            end = n
            reached_end = True
        for j in range(max(last_idx, i-k), end):
            cache[j] = min(new, cache[j])
        last_idx = end
print(cache[n-1])

