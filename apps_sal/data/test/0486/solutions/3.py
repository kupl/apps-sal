def pd(d):
    d = str(d)
    ans = 1
    for c in d:
        ans *= int(c)
    return ans
        

S = input()
D = int(S)
ans = pd(D)

if str(D)[0] == '1':
    ans = 9 ** (len(str(D)) - 1)
else:
    cur = 0
    while 10 ** cur < D:
        ans = max(ans, pd(D - (D % 10 ** cur) - 1))
        
        cur += 1 
        
print(ans)

