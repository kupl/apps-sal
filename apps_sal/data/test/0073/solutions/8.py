line = input()
nrs = list(map(int, line.split(' ')))
c = nrs[0]
v0 = nrs[1]
v1 = nrs[2]
a = nrs[3]
l = nrs[4]
pages_read = v0
days = 1
pages = v0
while pages_read < nrs[0]:
    pages += a
    if pages > v1:
        pages = v1
    pages_read -= l
    pages_read += pages
    days += 1

print(days)
