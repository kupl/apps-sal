n=int(input())
a=[int(i) for i in input().split()]

def somosomo(a):
    ans=[]
    if n%2==1:
        ans.append(0)
        for i in range(1,n//2+1):
            ans.append(i*2)
            ans.append(i*2)
        b=sorted(a)
        if b==ans:
            return True
        return False
    else:
        for i in range(1,n//2+1):
            ans.append(i*2-1)
            ans.append(i*2-1)
        b=sorted(a)
        if b==ans:
            return True
        return False

def two_ride(n):
    ans=1
    for i in range(n):
        ans*=2
        ans%=10**9+7
    return ans

if somosomo(a):
    print(two_ride(n//2))
else:
    print(0)
