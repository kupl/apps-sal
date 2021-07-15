n = int(input())
a = list(map(int, input().split()))

sol = 0
inv = [1, 0]

for i in range(0, n):
    for j in range(i, n):
        val = 0
        for k in range(0, n):
            if k < i or k > j: val += a[k]
            else: val += inv[a[k]]

        sol = max(sol, val)
            
print(sol)

