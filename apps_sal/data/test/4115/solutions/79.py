list_s = list(input())
count = 0
for i in range(0, len(list_s) // 2):
    if list_s[i] == list_s[0 - (i + 1)]:
        continue
    else: count += 1
print(count)
