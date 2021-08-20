t = int(input())
while t > 0:
    (n, x, y) = list(map(int, input().split()))
    min_val = 100000.0
    min_diff = 0
    for xpos in range(0, n - 1):
        for ypos in range(xpos + 1, n):
            l = ypos - xpos
            if (y - x) % l > 0:
                continue
            diff = (y - x) / l
            max_item = x + (n - 1 - xpos) * diff
            if max_item < min_val and x - xpos * diff >= 1:
                min_val = int(max_item)
                min_diff = int(diff)
    first_num = min_val - (n - 1) * min_diff
    for index in range(0, n):
        print('{}'.format(first_num + index * min_diff), end=' ')
    print('')
    t -= 1
