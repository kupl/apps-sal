n = int(input())
a = list(map(int,input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


adiv = sorted(set(make_divisors(a[0]) + make_divisors(a[1])),reverse=True)


def is_ok(arg):
    #print(f"index{arg}でーす{adiv[arg]}")
    cnt = 0
    for i in range(n):
        if a[i]%adiv[arg] != 0:
            cnt += 1
            #print(str(a[i])+"×")

        if cnt>=2:
            #print("だめ"+str(a[i])+" iは"+str(i))
            return False
            break    
    else:
        #print("ok-")
        return True

import sys
for i in range(len(adiv)):
    if is_ok(i):
        print(adiv[i])
        return
