n = int(input())
string = input()
arr = [str(i) for i in string][:n]
left = right = up = down = 0
for i in arr:
    if i == 'L':
        left += 1
    elif i == 'R':
        right += 1
    elif i == 'U':
        up += 1
    elif i == 'D':
        down += 1
print(2 * (min(left, right) + min(up, down)))
