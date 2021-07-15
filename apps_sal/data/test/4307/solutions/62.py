3
#coding: utf-8

N = int(input())

def num_div(n):
    ret = 0
    for i in range(1, n+1):
        if n % i == 0:
            ret+=1
    return ret

r = 0
for i in range(1, N+1, 2):
    if num_div(i) == 8:
        r += 1

print(r)
