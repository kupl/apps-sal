n, k = list(map(int, input().split()))

a = list(map(int, input().split())) + [-1]

cost = 0
lib = []

for i in range(n):
    if a[i] in lib:
        continue
    if len(lib) < k:
        lib.append(a[i])
        cost += 1
    else:
        far = 0
        for ind, j in enumerate(lib):
            o = i+1
            while o < n+1 and a[o] != j:
                o += 1
            if o > far:
                far = min(o, n-1)
                maxindex = ind
                maxele = j
                if o == n:
                    break
        lib[maxindex] = a[i]
        cost += 1

print(cost)

