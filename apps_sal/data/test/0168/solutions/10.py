n = int(input())
ops = input().strip()
begin = 0
for op in ops:
    if op == '-':
        begin -= 1
    elif op == '+':
        begin += 1

    begin = max(begin, 0)

print(begin)
