s = int(input())
def p(n):
    if n%2 ==0:
        return n//2
    else:
        return 3*n+1
l = [s]
cnt = 1
while True:
    cnt +=1
    s = p(s)
    if s in l:
        print(cnt)
        return
    else:
        l.append(s)
