t = int(input())

def conv1(v) :
    nonlocal z
    index, q = 0, 0
    for i in range(len(v)) :
        if v[i] == '(' : q += 1
        else : q -= 1
        if q == 0 and v[i] == '(' :
            if i != len(v) : v = v[:index] + list(reversed(v[index:i+1])) + v[i+1:]
            else : v = v[:index] + list(reversed(v[index:i+1]))
            z.append([index+1, i+1])
            index = i+1
        elif q == 0 : index = i+1
    return v

def count(v) :
    q, k = 0, 0
    for i in v :
        if i == '(' : q += 1
        else : q -= 1
        if q == 0 : k += 1
    return k

def conv_min(v, k, n) :
    nonlocal z
    q = 0
    for i in range(0, len(v)) :
        if k == n : return v
        if v[i] == '(' : q += 1
        else : q -= 1
        if q == 0 :
            z.append([i+1, i+2])
            n -= 1

def conv_max(v, k, n) :
    nonlocal z
    q = 0
    for i in range(0, len(v)) :
        if k == n : return v
        if v[i] == '(' : q += 1
        else :
            if q == 2 :
                v[i-1], v[i] = v[i], v[i-1]
                q = 1
                z.append([i, i+1])
                n += 1
            elif q > 2 :
                v[i-q+1], v[i] = v[i], v[i-q+1]
                z.append([i-q+1, i+1])
                z.append([i-q+1, i-q+2])
                q -= 1
                n += 1
            else : q = 0

if 1 == 2 :
    s = list('()(())')
    z = []
    print(''.join(conv_max(s, 3, 2)))
    raise SystemExit

for _ in range(t) :
    _, k = [int(x) for x in input().split()]
    s = list(input())
    z = []
    
    s = conv1(s)
    ct = count(s)
    if ct >= k : conv_min(s, k, ct)
    else : conv_max(s, k, ct)
    print(len(z))
    print('\n'.join(list([str(x[0])+' '+str(x[1]) for x in z])))

