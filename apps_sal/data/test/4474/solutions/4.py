# coding: utf-8
# Your code here!
def tobase3(n):
    a = []
    while(n > 0):
        a.append(n % 3)
        n //= 3
    a.reverse()
    return a


def todec(a):
    sum = 0
    for i in range(len(a)):
        sum *= 3
        sum += a[i]
    return sum


t = int(input())
for _ in range(t):
    n = int(input())
    a = tobase3(n)
    j = 0
    flag = False
    for i in range(len(a)):
        if(a[i] == 2):
            flag = True
            j = i
            while(j >= 0 and a[j] != 0):
                j -= 1
            break
    if(j < 0 and flag):
        print(3**len(a))
    elif(flag):
        print(todec(a[:j] + [1] + [0] * (len(a) - j - 1)))
    else:
        print(n)
