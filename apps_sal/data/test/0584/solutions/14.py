input()
s = input()

ans = ["", ""]
cur = 0
for c in s:
    if c == '(':
        ans[cur] += '_'
        cur += 1
    elif c == ')':
        ans[cur] += '_'
        cur -= 1
    else:
        ans[cur] += c
for i in range(2):
    ans[i] = ans[i].split('_')

# print(ans[0])
# print(ans[1])

print(max([0] + [len(w) for w in ans[0]]), sum(1 if w else 0 for w in ans[1]))
