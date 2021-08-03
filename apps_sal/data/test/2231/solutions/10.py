import sys


def read(): return sys.stdin.readline().strip()
def prcs(x, y): return (x + y)**2 / (x * y)


n = int(read())
for i in range(0, n):
    t = int(read())
    a = list(map(int, read().split()))
    a.sort()
    dub = []
    ind = 0
    while(ind < t - 1):
        if(a[ind] == a[ind + 1]):
            dub.append(a[ind])
            ind += 1
        ind += 1
    # print(dub)
    mn = prcs(dub[0], dub[1])
    index = 0
    for j in range(0, len(dub) - 1):
        if(mn > prcs(dub[j], dub[j + 1])):
            mn = prcs(dub[j], dub[j + 1])
            index = j
        # print(dub[j],dub[j+1],prcs(dub[j],dub[j+1]),mn,index)
    print(dub[index], dub[index], dub[index + 1], dub[index + 1])
