a,b = input().split()
ab = a*int(b)
ba = b*int(a)
s = max(len(ab),len(ba))

if s == len(ab) :
    print(ab)
else :
    print(ba)
