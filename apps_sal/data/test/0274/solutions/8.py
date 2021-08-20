n = int(input())
s = list(input())
max_len = 0
cur_len = 0
for si in s:
    if si == '[':
        cur_len += 1
    if si == ']':
        cur_len -= 1
    if cur_len > max_len:
        max_len = cur_len
cur_len = 0
size = []
ans = []
for si in s:
    if si == '[':
        cur_len += 1
        size.append(max_len - cur_len + 1)
        ans.append(size[-1])
    if si == ']':
        cur_len -= 1
        ans.append(size[-1])
        size = size[:-1]


def draw_bracket(pos, size, picture, open):
    start = (len(picture) - 2 * size - 1) // 2
    picture[start][pos] = '+'
    if open:
        picture[start][pos + 1] = '-'
    else:
        picture[start][pos - 1] = '-'
    picture[len(picture) - start - 1][pos] = '+'
    if open:
        picture[len(picture) - start - 1][pos + 1] = '-'
    else:
        picture[len(picture) - start - 1][pos - 1] = '-'
    for i in range(start + 1, len(picture) - start - 1):
        picture[i][pos] = '|'


def draw_picture(picture):
    for i in picture:
        print(''.join(i))


pic_size = 0
for i in range(n):
    pic_size += 1
    if i + 1 < n and s[i] == '[' and (s[i + 1] == ']'):
        pic_size += 3
picture = [[' '] * pic_size for i in range(2 * max_len + 1)]
pos = 0
for i in range(n):
    if s[i] == '[':
        draw_bracket(pos, ans[i], picture, True)
        if i + 1 < n:
            if s[i + 1] == '[':
                pos += 1
            if s[i + 1] == ']':
                pos += 4
    if s[i] == ']':
        draw_bracket(pos, ans[i], picture, False)
        pos += 1
draw_picture(picture)
