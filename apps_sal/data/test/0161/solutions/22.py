n = int(input())
def transform():
    nonlocal n
    s = bin(n)[2:]
    for i in range(len(s)):
        if s[i]=='0': break
    index = i
    res = ''
    for i in range(len(s)):
        if i>=index: res+='1'
    n = int(res, 2)^n
    return(len(res))
def check():
    nonlocal n
    s = bin(n)[2:]
    n+=1
    if '0' not in s: return True
    else: return False
cnt = 0
toprint = []
while True:
    s = bin(n)[2:]
    if '0' not in s:
        print(cnt)
        for i in toprint: print(i, end=' ')
        print()
        break
    toprint.append(transform())
    cnt+=1
    if check():
        print(cnt)
        for i in toprint: print(i, end=' ')
        print()
        break
    cnt+=1

