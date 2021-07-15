def RPS(a,b):
    if a == b:
        return a
    elif a == 'R' and b == 'S':
        return a
    elif a == 'P' and b == 'R':
        return a
    elif a == 'S' and b == 'P':
        return a
    else:
        return b

n,k = map(int, input().split())
s= input()

while k > 0:
    t = s + s
    s = []
    for i in range(0,len(t),2):
        s.append(RPS(t[i],t[i+1]))

    k -= 1
print(s[0])
