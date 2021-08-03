nk = input().split()
n = int(nk[0])
k = int(nk[1])
p_s = input().split()
p = [int(s) for s in p_s]
max_val = 0
for i in range(0, k):
    max_val += p[i]
tmp = max_val
for i in range(k, len(p)):
    tmp = tmp - p[i - k] + p[i]
    if tmp > max_val:
        max_val = tmp
print(max_val / 2 + 0.5 * k)
