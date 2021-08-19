w, m, k = list(map(int, input().split()))
#print('w='+str(w)+' m='+str(m)+' k='+str(k))
n = m - 1
l = len(str(m))
# print('l='+str(l))
while w > 0:
    t = ((10**l) - n - 1) * l * k
    # print('t='+str(t))
    if w <= t:
        n += w // (l * k)
        w = 0
    else:
        n = 10**l
        w = w - t - (l + 1) * k
        l += 1
    #print('n='+str(n)+' w='+str(w))
print(n - m + 1)
