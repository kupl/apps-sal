good = set(input().strip())
pattern = input().strip()
n = int(input())
minlen = len(pattern)
is_star = '*' in pattern
if is_star:
    minlen -= 1
    maxlen = 1000000000
    leftlen = pattern.find('*')
    rightlen = len(pattern) - leftlen - 1
else:
    maxlen = minlen


def check_simple_pattern(task, pattern):
    for i in range(len(task)):
        if pattern[i] != task[i] and (not (pattern[i] == '?' and task[i] in good)):
            return False
    return True


def check(task):
    if len(task) < minlen or len(task) > maxlen:
        return False
    if is_star:
        if rightlen == 0:
            cond = all([i not in good for i in task[leftlen:]])
        else:
            cond = all([i not in good for i in task[leftlen:-rightlen]])
        return check_simple_pattern(task[:leftlen], pattern[:leftlen]) and (rightlen == 0 or check_simple_pattern(task[-rightlen:], pattern[-rightlen:])) and cond
    else:
        return check_simple_pattern(task, pattern)


for i in range(n):
    task = input().strip()
    if check(task):
        print('YES')
    else:
        print('NO')
