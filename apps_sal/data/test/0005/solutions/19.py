(n, pos, l, r) = [int(i) for i in input().split()]
seconds = 0
if l > 1:
    seconds += 1
    if abs(pos - l) < abs(pos - r) or r == n:
        seconds += abs(pos - l)
    else:
        seconds += r - l
if r < n:
    seconds += 1
    if abs(pos - l) >= abs(pos - r) or l == 1:
        seconds += abs(pos - r)
    else:
        seconds += r - l
print(seconds)
