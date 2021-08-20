(n, p) = map(int, input().split())
total = 0
sold = 0.0
log = []
for i in range(n):
    log.append(input() == 'half')
for x in reversed(log):
    if x:
        total *= 2
        sold += total / 2
    else:
        total = total * 2 + 1
        sold += total / 2
print(int(sold * p))
