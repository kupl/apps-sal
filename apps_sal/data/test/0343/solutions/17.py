n, k, p, x, y = [int(k) for k in input().split()]
scores = [int(k) for k in input().split()]
s = sum(scores)
number_needed = (n - 1) / 2
B = x - s
done = False

while not done:
    num_above = 0
    num_below = 0
    for i in scores:
        if i >= y:
            num_above += 1
        else:
            num_below += 1
    num_needed_above = int(number_needed + 1 - num_above)
    num_needed_below = int(number_needed - num_below)
    if num_needed_below < 0:
        print(-1)
        break
    if num_needed_above < 0:
        num_needed_above = 0
        num_needed_below = n - k
    rem_sum = y * num_needed_above + 1 * num_needed_below
    if rem_sum <= B:
        for i in range(num_needed_below):
            print(1, end=" ")
        for i in range(num_needed_above):
            print(y, end=" ")
        done = True
    else:
        y = y + 1
        if y > p:
            print(-1)
            break
