def remainderSet(n, k):
    rem=set()
    for i in range(1,k+1):
        r=n%i
        if r in rem:
            return False
        else:
            rem.add(r)
    return True

def test():
    print(remainderSet(4,4))
    print(remainderSet(5,3))

def nia():
    s=input()
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal

def solve():
    arr=nia()
    if remainderSet(arr[0], arr[1]):
        print("Yes")
    else:
        print("No")
        
solve()

