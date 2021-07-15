l = [0]

t = int(input())
def count(level):
    nums = 10**level - 10**(level - 1)
    first = l[level - 1] + level
    last = l[level - 1] + nums*level
    if len(l) <= level:
        l.append(last)
    return (nums*(first+last))//2

def search(min_size,val,level):
    checker = val*min_size + level*(val*(val + 1))//2
    return checker

for _ in range(t):
    ind = int(input())
    level = 1
    while ind > count(level):
        ind -= count(level)
        level += 1

    min_size = l[level-1]

    lo = 0
    hi = 10**level - 10**(level-1)

    while hi - lo > 1:
        val = (hi+lo)//2
        checker = search(min_size,val,level)
        if checker < ind:
            lo = val
        else:
            hi = val

    ind -= search(min_size,lo,level)

    new_l = 1
    while 9*(10**(new_l-1))*new_l < ind:
        ind -= 9*(10**(new_l-1))*new_l
        new_l += 1

    ind -= 1

    more = ind // new_l
    dig = ind % new_l
    value = 10 ** (new_l - 1) + more
    print(str(value)[dig])


