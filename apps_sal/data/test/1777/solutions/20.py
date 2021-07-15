n = int(input())

left = {}
right = {}
neutral_count = 0

for _ in range(n):
    bracket = input()
    s = []
    for p in bracket:
        if '(' == p:
            s.append('(')
        if ')' == p:
            if len(s) > 0 and s[-1] == '(':
                s.pop()
            else:
                s.append(')')
    if len(s) == 0:
        neutral_count += 1
    elif all(e == '(' for e in s):
        l = len(s)
        if l in left:
            left[l] += 1
        else:
            left[l] = 1
    elif all(e == ')' for e in s):
        r = len(s)
        if r in right:
            right[r] += 1
        else:
            right[r] = 1
ans = 0
ans += neutral_count//2
for l in left:
    r = 0
    if l in right:
        r = right[l]
    ans += min(left[l], r)
print(ans) 



