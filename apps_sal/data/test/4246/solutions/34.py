slist = list(input())
tlist = list(input())

slist_new = [slist[0] + '0', slist[1] + '1', slist[2] + '2']
tlist_new = [tlist[0] + '0', tlist[1] + '1', tlist[2] + '2']

list02 = slist_new + tlist_new
andlist = [x for x in list02 if list02.count(x) > 1]

print((len(andlist) // 2))

