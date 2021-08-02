n, x, m = list(map(int, input().split()))
x %= m
d = {x: 1}
arr = [0] * (m + 1)
arr[1] = x
for i in range(2, n + 1):
    x = (x * x) % m
    if x in d:
        start = d[x]
        end = i - 1
        sumPreCycle = sum(arr[1:start])
        numPreCycle = start - 1
        lenCycle = end - start + 1
        sumCycle = sum(arr[start:end + 1])
        numCycle = (n - numPreCycle) // lenCycle
        numAfterCycle = n - numPreCycle - lenCycle * numCycle
        sumAfterCycle = sum(arr[start:start + numAfterCycle])
        print((sumPreCycle + sumAfterCycle + sumCycle * numCycle))
        break
    else:
        arr[i] = x
        d[x] = i
else:
    print((sum(arr[1:n + 1])))
