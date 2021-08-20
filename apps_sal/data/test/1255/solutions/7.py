checkouts = 0
max_checkouts = 0
time = ''
customers = int(input())
for i in range(customers):
    next_time = input()
    if next_time == time:
        checkouts += 1
    else:
        max_checkouts = max(max_checkouts, checkouts)
        checkouts = 0
        time = next_time
max_checkouts = max(max_checkouts, checkouts)
print(max_checkouts + 1)
