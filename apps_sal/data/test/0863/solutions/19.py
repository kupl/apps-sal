s = input().split()
a = int(s[0])
ta = int(s[1])
s = input().split()
b = int(s[0])
tb = int(s[1])
s = input().split(':')
hh = int(s[0])
mm = int(s[1])
starttime = hh * 60 + mm
endtime = starttime + ta
i = 300
l = []
while i < 1440:
    l.append(i)
    i += b
length = len(l)
c = 0
for i in range(0, length):
    if l[i] < endtime and l[i] + tb > starttime:
        c += 1
print(c)
