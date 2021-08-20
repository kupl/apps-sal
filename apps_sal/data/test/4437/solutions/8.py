n = int(input())
l = [*input()]
a = b = 0
cnt = 0
for i in range(n):
    if l[i] == 'a':
        a += 1
    else:
        b += 1
    if i & 1 and a != b:
        cnt += 1
        if a > b:
            (l[i], a) = ('b', b)
        else:
            (l[i], b) = ('a', a)
print(cnt)
print(''.join(l))
