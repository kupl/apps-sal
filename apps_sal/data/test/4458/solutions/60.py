n = int(input()); a = [*map(int, input().split())]; count, m = 0, n + 1
for i in a:
    if m > i: m = i; count += 1
print(count)
