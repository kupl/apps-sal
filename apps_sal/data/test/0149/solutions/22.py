def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    nonlocal input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


x = get_number()
y = get_number()
l = get_number()
r = get_number()
n1 = 1;
a = list()
a.append(l - 1)
for i in range(0, 300):
    if n1 > r:
        break
    n2 = 1 
    for j in range(0, 300):
        if n1 + n2 > r:
            break
        if n1 + n2 >= l and n1 + n2 <= r:
            a.append(n1 + n2)
        n2 = n2 * y
    n1 = n1 * x
    
a.append(r + 1)
a.sort()
ans = 0
for i in range(0, len(a) - 1):
    ans = max(ans, a[i + 1] - a[i] - 1)
print(ans)
