n, t, c = [int(c) for c in input().split()]
cruelty = [int(c) for c in input().split()]
res = 0
current_length = 0

for i in cruelty:
    if i <= t:
        current_length += 1
    else:
        if current_length >= c:
            res += current_length - c + 1
        current_length = 0

if current_length >= c:
    res += current_length - c + 1

print(res)
