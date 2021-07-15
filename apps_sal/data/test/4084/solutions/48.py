a,b,c = list(map(int,(input().split())))
d = (a//(b+c))*b + min((a%(b+c)),b)
print(d)

