s = input()
t = input()
 
sp = sorted(s)
tp = sorted(t, reverse=True)
#print(sp, tp)
print(('Yes' if sp < tp else 'No'))

