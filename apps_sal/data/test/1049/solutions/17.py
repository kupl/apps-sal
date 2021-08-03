n, d = map(int, input().split())
ch = []
c_ch = 0
for i in range(d):
    a = input()
    if '0' in a:
        c_ch += 1
    else:
        ch.append(c_ch)
        c_ch = 0
ch.append(c_ch)
print(max(ch))
