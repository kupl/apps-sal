n = int(input())
s = input()
t = set()
for i in range(n):
    t.add(ord(s[i]))
l = len(t)
o = dict()
p = 0
i = 0
while p < l:
    r = o.get(ord(s[i]), 0)
    if r == 0:
        o[ord(s[i])] = 1
        p += 1
    else:
        o[ord(s[i])] += 1
    i += 1
left = 0
minn = i - left
while True:
    if o[ord(s[left])] > 1:
        o[ord(s[left])] -= 1
        left += 1
        minn = min(minn, i - left)
    else:
        if i >= n:
            break
        o[ord(s[i])] += 1
        i += 1
print(minn)
