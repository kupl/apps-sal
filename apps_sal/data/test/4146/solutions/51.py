n = int(input())
v = list(map(int, input().split()))
odd = dict()
even = dict()
odd[-1] = 0
even[-1] = 0

for i in range(n):
    if (i + 1) % 2 == 1:
        if v[i] not in odd:
            odd[v[i]] = 1
        else:
            odd[v[i]] += 1
    else:
        if v[i] not in even:
            even[v[i]] = 1
        else:
            even[v[i]] += 1

odd_values = sorted(list(odd.values()), reverse=True)
for key, val in list(odd.items()):
    if val == odd_values[0]:
        odd_1 = key
    elif val == odd_values[1]:
        odd_2 = key

even_values = sorted(list(even.values()), reverse=True)
for key, val in list(even.items()):
    if val == even_values[0]:
        even_1 = key
    elif val == even_values[1]:
        even_2 = key

if odd_1 != even_1:
    res = n - odd_values[0] - even_values[0]
else:
    res = min(n - odd_values[0] - even_values[1],
              n - odd_values[1] - even_values[0])
print(res)
# print(odd)
# print(even)
