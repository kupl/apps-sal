s = list(map(int,input().split(':')))
s = (24+s[0])*60+s[1]
t = list(map(int,input().split(':')))
t = t[0]*60+t[1]
p = (s - t) % (24 * 60)
p = '{:02}:{:02}'.format(p//60, p % 60)
print(p)

