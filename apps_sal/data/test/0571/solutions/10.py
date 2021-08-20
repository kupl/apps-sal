input()
s = input()
if len(s) & 1:
    print(':(')
    raise SystemExit(0)
(max_open, min_open) = (0, 0)
started = False
q_mark = 0
op = 0
cl = 0
ended = False
for c in s:
    if ended:
        print(':(')
        raise SystemExit(0)
    if min_open <= 0 and started:
        min_open = 1
    started = True
    if c == '(':
        op += 1
        max_open += 1
        min_open += 1
    elif c == ')':
        cl += 1
        max_open -= 1
        min_open -= 1
    else:
        q_mark += 1
        max_open += 1
        min_open -= 1
    if max_open < 1:
        ended = True
if min_open != 0:
    print(':(')
    raise SystemExit(0)
s = list(s)
open_count = len(s) // 2 - op
for i in range(len(s)):
    if s[i] == '(':
        op -= 1
    elif s[i] == ')':
        cl -= 1
    elif s[i] == '?':
        if open_count == 0:
            s[i] = ')'
        else:
            s[i] = '('
            open_count -= 1
print(''.join(s))
