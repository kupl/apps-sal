(n, m) = list(map(int, input().split()))
bulbs = set(range(1, m + 1))
for _ in range(n):
    (count, *numbers) = list(map(int, input().split()))
    for number in numbers:
        bulbs -= {number}
if len(bulbs) > 0:
    print('NO')
else:
    print('YES')
