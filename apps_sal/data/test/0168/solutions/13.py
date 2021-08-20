n = int(input())
ops = input()
resp = 0
for op in ops:
    if op == '-':
        resp = max(0, resp - 1)
    else:
        resp += 1
print(resp)
