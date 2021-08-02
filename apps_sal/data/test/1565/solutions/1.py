import math


def f(R):
    if R == 0:
        return 0
    F = 0; S = 0; cur = 1
    for i in range(150):
        t = min(cur, R - F - S)
        #print(str(i)+' '+str(F)+' '+str(S)+' '+str(t))
        if i % 2 == 0:
            F = F + t
        else:
            S = S + t
        cur = cur * 2
        if R == F + S:
            break
    ans = F * F + S * S + S
    return ans

#L,R = map(int,input().strip().split())
#L = L-1
#ans = f(R)-f(L)
#ans = ans%1000000007
# print(ans)


n = int(input())
s = input()
ans = int(s)
for i in range(n // 2, n):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
for i in range(n // 2, 0, -1):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
for i in range(n // 2 + 1, n):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
for i in range(n // 2 + 1, 0, -1):
    if s[i] != '0':
        a = int(s[:i])
        b = int(s[i:])
        ans = min(ans, a + b)
        break
print(ans)
# V=[1]
# it=1
# den=1
# flag=0
# x=0
# for i in range(N):
# s=input()
##    s+=" last"
# s=s.strip().split()
# if s[0]=="for":
# n=int(s[1].strip())
# if it>2**32:
# n=1
# it*=n
# V.append(n)
# elif s[0]=="add":
# x+=it
# if x>=2**32:
# flag=1
# break
# elif s[0]=="end":
# it/=V[-1]
# V.pop()
# print(str(s)+" "+str(x)+" "+str(it)+" "+str(V))
# if flag==1:
# print("OVERFLOW!!!")
# else:
# print(int(x))
# t=[1]
# while t[len(t)-1]*2<=n:
# t.append(t[-1]*2)
# x=0
# i=0
# while i<len(t) and x+t[i]<=n:
# x=x+t[i]
# i=i+1
##
# if n&(n+1)==0:
# print n
# elif k==1:
# print n
# else:
# print 2*t[-1]-1
