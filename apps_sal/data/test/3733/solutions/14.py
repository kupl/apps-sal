import math

n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))

lst.sort()
last_val = -1
freq_list = []

for i in range(n):
    if lst[i] != last_val:
        last_val = lst[i]
        freq_list.append(1)
    else:
        freq_list[-1] += 1

k = len(freq_list)

for i in range(k, 0, -1):
    if n * math.ceil(math.log2(i)) <= m * 8:
        k = i
        break

mx = 0
tot = sum(freq_list[:k])
mx = max(tot, mx)
for i in range(k, len(freq_list)):
    tot = tot + freq_list[i] - freq_list[i - k]
    mx = max(mx, tot)

print(n - mx)
