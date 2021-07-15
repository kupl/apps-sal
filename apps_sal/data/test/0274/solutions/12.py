def draw(ind, type, size):
    nonlocal ans, mid
    ans[mid][ind] = '|'
    for i in range(size // 2):
        ans[mid + i][ind] = '|'
        ans[mid - i][ind] = '|'
    ans[mid + size // 2][ind] = '+'
    ans[mid - size // 2][ind] = '+'
    if type == "left":
        ans[mid + size // 2][ind - 1] = '-'
        ans[mid - size // 2][ind - 1] = '-'
    else:
        ans[mid + size // 2][ind + 1] = '-'
        ans[mid - size // 2][ind + 1] = '-'


n = int(input())
s = input()
mx = 0
cs = 0
for i in range(n):
    if s[i] == "[":
        cs += 1
    else:
        cs -= 1
    mx = max(mx, cs)
mx -= 1
a = [mx]
for i in range(1, n):
    if (s[i] == "[" and s[i - 1] == "]") or (s[i - 1] == "[" and s[i] == "]"):
        a.append(a[-1])
    elif s[i] == "[":
        a.append(a[-1] - 1)
    else:
        a.append(a[-1] + 1)
ans = [[' ' for i in range(n * 3)] for j in range(3 + mx * 2)]
mid = mx + 1
draw(0, "right", mx * 2 + 3)
li = 0
for i in range(1, n):
    if s[i] == "[" and s[i - 1] == "]":
        li += 1
        draw(li, "right", a[i] * 2 + 3)
    elif s[i - 1] == "[" and s[i] == "]":
        li += 4
        draw(li, "left", a[i] * 2 + 3)
    elif s[i] == "[":
        li += 1
        draw(li, "right", a[i] * 2 + 3)
    else:
        li += 1
        draw(li, "left", a[i] * 2 + 3)
for i in ans:
    for j in range(li + 1):
        print(i[j], end="")
    print()

