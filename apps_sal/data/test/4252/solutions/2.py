l = int(input())

s = input()

count = 0
res = 0
for c in s:
    if c == 'x':
        count += 1
    else:
        res += max(0, count - 2)
        count = 0
res += max(0, count - 2)
print(res)
