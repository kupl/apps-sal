import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''

a, b, x = map(int, input().split())
if a * 10**9 + b * 10 < x:
    print(10**9)
    return


def bisearch(n):
    left = 1
    right = 10**9
    maxbuy = 0
    while left <= right:
        mid = (left + right) // 2
        now = a * mid + b * len(str(mid))
        if now <= x and now > maxbuy:
            maxbuy = mid
        if now > x:
            right = mid - 1
        else:
            left = mid + 1
    return maxbuy


print(bisearch(x))
