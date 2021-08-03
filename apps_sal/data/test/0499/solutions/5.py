n = int(input())
s = input().strip()
if 'R' in s and 'G' in s and 'B' in s:
    ans = "RGB"
elif 'R' in s and 'G' in s:
    a = 'R'
    b = 'G'
    c = 'B'
    if s.count(a) > 1 and s.count(b) > 1:
        ans = "RGB"
    else:
        if n == 2:
            ans = c
        else:
            if s.count(a) > s.count(b):
                ans = b + c
            else:
                ans = a + c
elif 'R' in s and 'B' in s:
    a = 'R'
    c = 'G'
    b = 'B'
    if s.count(a) > 1 and s.count(b) > 1:
        ans = "RGB"
    else:
        if n == 2:
            ans = c
        else:
            if s.count(a) > s.count(b):
                ans = b + c
            else:
                ans = a + c
elif 'G' in s and 'B' in s:
    c = 'R'
    a = 'G'
    b = 'B'
    if s.count(a) > 1 and s.count(b) > 1:
        ans = "RGB"
    else:
        if n == 2:
            ans = c
        else:
            if s.count(a) > s.count(b):
                ans = b + c
            else:
                ans = a + c
else:
    ans = s[0]
ret = []
for char in ans:
    ret.append(char)
ret.sort()
print(''.join(ret))
