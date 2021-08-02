N = int(input())
operations = input()

res = 0
for c in operations:
    if c == '-':
        res = max(0, res - 1)
    else:
        res += 1

print(res)
