n = int(input())
lst = list(input())
count = 0
for i in range(0, len(lst)):
    if lst[i - 2] == 'A' and lst[i - 1] == 'B' and lst[i] == 'C':
        count += 1

print(count)
