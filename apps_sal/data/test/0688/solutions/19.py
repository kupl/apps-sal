a = input()
b = input()

d = {}
for e in b:
    if e == '9':
        e = '6'
    if e == '5':
        e = '2'
    if e in d:
        d[e] = d[e] + 1
    else:
        d[e] = 1

n = {}
for e in a:
    if e == '9':
        e = '6'
    if e == '5':
        e = '2'
    if e in n:
        n[e] += 1
    else:
        n[e] = 1
result = 10000000
for e in n:
    if e not in d:
        result = 0
        break
    else:
        temp_result = int(d[e] / n[e])
        if temp_result < result:
            result = temp_result

print(result)
