N = int(input())
S_list = [input() for _ in range(N)]

min_revr, min_revl = 10**20, 10**20
left, rev_l, rev_r, right = 0, 0, 0, 0
for S in S_list:
    stack = []
    l, r = 0, 0
    for s in S:
        if s == '(':
            if stack:
                if stack[-1] == ')':
                    stack.append('(')
                    l = 1
                else:
                    stack.append('(')
                    l += 1
            else:
                stack.append('(')
                l = 1
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                    l -= 1
                else:
                    stack.append(')')
                    r += 1
            else:
                stack.append(')')
                r = 1
    if l == 0:
        right += r
    elif r == 0:
        left += l
    else:
        rev_r += r
        rev_l += l
        min_revr = min(min_revr, r)
        min_revl = min(min_revl, l)

if min_revr == 10**20:
    min_revr = 0
if min_revl == 10**20:
    min_revl = 0

if left + rev_l == rev_r + right and left >= min_revr and right >= min_revl:
    print('Yes')
else:
    print('No')
