n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
s = sum(a)
dl = []
for i in range(1,int(s**0.5)+1):
    if s%i == 0:
        dl.append(i)
        if i != s//i:
            dl.append(s//i)
dl.sort(reverse = True)

def search(x):
    ml = []
    for i in a:
        ml.append(i%x)
    ml.sort(reverse = True)
    ms = sum(ml)
    count = 0
    i = 0
    while k > count and ms > count:
        mi = x-ml[i]
        if k >= mi:
            count += mi
            ms -= ml[i]
            
        else:
            break
        i += 1

    if k >= count and count == ms:
        return True
    else:
        return False

for i in dl:
    
    if search(i):
        print(i)
        return


