l = list(map(int, input().split()))
l.sort(reverse=True)
print(10*l[0]+1*l[1]+l[2])
