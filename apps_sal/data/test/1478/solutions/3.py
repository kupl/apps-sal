line = input()
line = line.split(',')
A = 'abcdefghijklmnopqrstuvwxyz'
depth = 1
comments = [[]]
cur_cnt, cur_depth = [0], 1

for token in line:
    if token[0] in A or token[0] in A.upper():
        comments[cur_depth - 1].append(token)
        cur_cnt[cur_depth - 1] -= 1
    else:
        cnt = int(token)
        if cnt > 0:
            cur_depth += 1
            if cur_depth > len(cur_cnt):
                cur_cnt.append(0)
            cur_cnt[cur_depth - 1] = cnt
            if cur_depth > depth:
                comments.append([])
                depth = max(cur_depth, depth)
        else:
            while cur_depth > 1 and cur_cnt[cur_depth - 1] == 0:
                cur_depth -= 1

print(len(comments))
for line in comments:
    print(' '.join(line))
