li = ['MON','TUE','WED','THU','FRI','SAT','SUN']

n = input()

if n == 'SUN':
    print(7)
else:
    print(6 - li.index(n))
