S = list(input())
count = 0
t = ''
for i in S:
    if t == i:
        continue
    else:
        t = i
        count += 1
print(count - 1)
