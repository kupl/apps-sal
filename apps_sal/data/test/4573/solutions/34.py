a = int(input())
b = list(map(int,input().split()))

c = sorted(b, reverse=True)

m = int(a / 2) - 1
anslist = [0] * a
for i, data in enumerate(b):
    if c[m] > data:
        anslist[i] = c[m]
    elif c[m] <= data:
        anslist[i] = c[m + 1]
        
for j in range(a):
    print(anslist[j])
