a, b, k = map(int,input().split())

c = []

for i in range(1,b+1):
    if a % i == 0 and b % i ==0:
        c.append(i)
    else:
        pass

print(c[-k])
