n = int(input())
s = input() + '_'
s_ = 0
c = 0
for i in s:
    if i == 'x':
        c += 1
    else:
        if c > 2:
            s_ += c - 2
        c = 0
print(s_)
