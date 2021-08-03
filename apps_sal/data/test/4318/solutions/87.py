n = int(input())
h = list(map(int, input().split()))
res = 1
h_max = h[0]
for i in range(1, len(h)):
    if h[i] >= h_max:
        res += 1
        h_max = h[i]
print(res)
