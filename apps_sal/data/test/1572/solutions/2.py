line = input()

integers = [int(i) for i in line.split()]
n = integers[0]

line = input()
values = [int(i) for i in line.split()]

if n > 1:
    longest = 2
    cur = 2
else:
    longest = 1
    cur = 1

for i in range(len(values)-2):
    if values[i] + values[i+1] == values[i+2]:
        cur += 1
    else:
        if cur > longest:
            longest = cur
        if n > 1:
            cur = 2
        else:
            cur = 1

if cur > longest:
    longest = cur

print(longest)

