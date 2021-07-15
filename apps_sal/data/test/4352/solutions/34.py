a, b = list(map(int, input().split()))
if a == 1: a = 14
if b == 1: b = 14
print(('Alice' if a > b else 'Bob' if a < b else 'Draw'))

