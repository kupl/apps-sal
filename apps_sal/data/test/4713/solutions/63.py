n = int(input())
s = list(input())
count = 0
max = 0
for i in range(n):
    if s[i] == 'I':
        count += 1
        if max < count:
            max = count
    elif s[i] == 'D':
        count -= 1
print(max)
