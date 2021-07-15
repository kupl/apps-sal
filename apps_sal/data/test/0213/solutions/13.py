def first(n, m, line):
    for i in range(0, n): 
        k, f = list(map(int, input().split())) 
        res = [] 
        for j in range(1, 101): 
            if j * f >= k and j * (f - 1) < k: 
                res.append(j) 
        line.append(res) 
        res = [] 
    return line


def check(n, m, hz):
    for i in range(1, 101): 
        dno = 0 
        for elem in line: 
            if i in elem: 
                dno += 1 
        if dno == n: 
            hz.append(i)
    return hz


m, n = list(map(int, input().split())) 
line = [] 
line = first(n, m, line)
hz = [] 
hz = check(n, m, hz)
ans = [] 

for element in hz: 
    if m % element == 0: 
        ans.append(m // element)
    else: 
        ans.append(m // element + 1)
smth = ans[0] 
answ = 0 
for element in ans: 
    if element != smth: 
        answ = -1 
if answ == -1: 
    print(answ) 
else: 
    print(smth)

