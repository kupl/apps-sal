N = int(input())
a = list(map(int,input().split()))
mode = [0]*(10**5+2)
for i in range(len(a)):
    k = a[i]
    if(a == 0):
        mode[k] += 1
        mode[k+1] += 1
    else:
        mode[k-1] += 1
        mode[k]   += 1
        mode[k+1] += 1

print(max(mode))
