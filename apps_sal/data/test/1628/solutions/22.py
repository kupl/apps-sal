from collections import Counter
def get_ans():
    c = Counter(input())
    x = c['x']
    y = c['y']
    if x > y:
        return 'x'*(x-y)
    elif y > x:
        return 'y'*(y-x)
    else:
        return ''
ans = get_ans()
print(ans)
