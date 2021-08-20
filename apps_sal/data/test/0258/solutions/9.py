n = int(input())
ticket = input()
left = right = diff = 0
for i in range(n // 2):
    if ticket[i] == '?':
        left += 1
    else:
        diff += int(ticket[i])
for i in range(n // 2, n):
    if ticket[i] == '?':
        right += 1
    else:
        diff -= int(ticket[i])
if left > right:
    temp = left
    left = right
    right = temp
    diff = -diff
bad = (right - left) // 2 * 9
if diff == bad:
    print('Bicarp')
else:
    print('Monocarp')
