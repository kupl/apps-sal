s = input()
p = s.find(':')
h = int(s[:p])
m = int(s[p + 1:])
a = int(input())
m = m + 60 * h + a
m %= 1440
print('%02d:%02d' % (m // 60, m % 60))
