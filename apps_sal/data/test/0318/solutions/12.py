3
(h, m) = tuple(map(int, input().split(':')))
a = int(input())
h = (h + (m + a) // 60) % 24
m = (m + a) % 60
if h < 10:
    print('0' + str(h), end='')
else:
    print(str(h), end='')
print(':', end='')
if m < 10:
    print('0' + str(m), end='')
else:
    print(str(m), end='')
