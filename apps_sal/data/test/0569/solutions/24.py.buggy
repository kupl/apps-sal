import sys

n = int(input())

if n > 26:
    print('-1')
    return

input_str = input()
res = 0
symbols = set()
for it in input_str:
    if it in symbols:
        res += 1
    else:
        symbols.add(it)
print(res)
