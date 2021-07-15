s = input()
q = int(input())

head = ''
tail = ''
rev = False
for _ in range(q):
    ql = list(input().split())

    if ql[0] == '1':
        head, tail = tail, head
        if rev:
            rev = False
        else:
            rev = True
    else:
        if ql[1] == '1':
            head += ql[2]
        else:
            tail += ql[2]

if rev:
    ans = head[::-1] + s[::-1] + tail
else:
    ans = head[::-1] + s + tail

print(ans)
