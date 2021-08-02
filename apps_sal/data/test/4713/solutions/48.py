N = int(input())
S = str(input())
max_int = 0
count = 0
for i in S:
    if i == 'I':
        count += 1
        max_int = max(max_int, count)
    elif i == 'D':
        count -= 1
print(max_int)
