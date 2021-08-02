n = int(input())
max_a = 0
next_a = 0
max_loc = 0
for i in range(n):
    ai = int(input())
    if ai > max_a:
        max_a = ai
        max_loc = i
    elif ai > next_a:
        next_a = ai
if next_a == 0:
    for i in range(n):
        print(max_a)
else:
    for i in range(max_loc):
        print(max_a)
    print(next_a)
    for i in range(n - max_loc - 1):
        print(max_a)
