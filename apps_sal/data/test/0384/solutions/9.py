n, s = int(input()), input()
cnt = [0]
for c in s:
    if c == 'B':
        cnt[-1] += 1
    elif cnt[-1]:
        cnt.append(0)
if not cnt[-1]:
    cnt.pop()
print(len(cnt))
print(*cnt)
