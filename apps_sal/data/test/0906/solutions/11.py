mo = 1000000007

def fast_pow(p):
    if (p == 0):
        return 1
    if (p % 2 == 1):
        return 2 * ((fast_pow(p//2) ** 2) % mo)

    return (fast_pow(p//2) ** 2) % mo 


arr = (input()).split(' ')

n = int(arr[0])
m = int(arr[1])
k = int(arr[2])

if ((n+m) % 2 == 1 and k == -1):
    print('0')
else:
    print (fast_pow(( n-1)*(m-1) ) % mo)
