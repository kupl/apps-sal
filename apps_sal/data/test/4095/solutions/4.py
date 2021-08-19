(n, m) = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))
smaller_greater = [(0, 0)]
for k in numbers:
    (s, g) = smaller_greater[-1]
    if k < m:
        smaller_greater.append((s + 1, g))
    elif k > m:
        smaller_greater.append((s, g + 1))
    else:
        smaller_greater.append((s, g))
i = numbers.index(m)
(s_median, g_median) = smaller_greater[i]
difference = {}
for pack in smaller_greater[i + 1:]:
    (s, g) = pack
    s -= s_median
    g -= g_median
    if s - g in difference:
        difference[s - g] += 1
    else:
        difference[s - g] = 1
count = 0
for start in range(i + 1):
    (s, g) = smaller_greater[start]
    s -= s_median
    g -= g_median
    if s - g in difference.keys():
        count += difference[s - g]
    if s - g - 1 in difference.keys():
        count += difference[s - g - 1]
print(count)
