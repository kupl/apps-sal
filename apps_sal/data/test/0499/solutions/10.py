n = int(input())
c = (lambda s: {(s.count(color), color) for color in 'BGR' if s.count(color)})(input())
if len(c) == 3 or (len(c) == 2 and min(c)[0] > 1):
    print('BGR')
elif len(c) == 1:
    print(min(c)[1])
elif max(c)[0] > 1:
    print(*sorted(set('BGR') - {max(c)[1]}), sep='')
else:
    print(*(set('BGR') - {x[1] for x in c}))
