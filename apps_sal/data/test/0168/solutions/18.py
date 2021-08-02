n = int(input())
s = input()
start = 0
for x in s:
    if x == '-':
        start = max(0, start - 1)
    else:
        start += 1
print(start)
