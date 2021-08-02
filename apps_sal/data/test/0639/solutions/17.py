# python3

numbers_nr, evil_value = (int(x) for x in input().split())
numbers = [int(x) for x in input().split()]

ans = 0
if evil_value in numbers:
    ans += 1
for value in range(0, evil_value):
    if value not in numbers:
        ans += 1

print(ans)
