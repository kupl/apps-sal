N = int(2e5+3)
cum = [0] * N
n, k = list(map(int, input().split()))
arr = [0] * n
for i in range(n):
    arr[i] = [[0,0], i+1]
    arr[i][0] = list(map(int, input().split()))    
    cum[arr[i][0][0]] += 1
    cum[arr[i][0][1]+1] -= 1
for i in range(1, N):
    cum[i] += cum[i-1]
arr.sort()
st = set()
res, j, prev = [], 0, 0
rmv = [0] * N
for i in range(N):
    while j < n and arr[j][0][0] <= i:
        st.add((arr[j][0][1], arr[j][1]))
        j += 1
    prev -= rmv[i]
    while len(st) > 0 and cum[i] - prev > k:
        it = max(st)
        st.remove(it)
        res.append(it[1])
        rmv[it[0]+1] += 1
        prev += 1

print(len(res))
print(*res)

