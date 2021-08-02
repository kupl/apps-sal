s = input()

left = ['*']
cnt = 0
for ch in s:
    if ch == left[-1]:
        left.pop()
        cnt += 1
    else:
        left.append(ch)

print(['No', 'Yes'][cnt % 2])
