def find(a,b,x,y,n):
    req = a-x
    min_val = min(req,n)
    a -= min_val
    n -= min_val
    b -= n

    return a*b

def solve(a,b,x,y,n,ans):
    req1 = a-x
    req2 = b-y
    if req1+req2 <= n:
        a = x
        b = y
        ans.append(str(a*b))
    else:
        min_val = find(a,b,x,y,n)
        min_val = min(min_val,find(b,a,y,x,n))
        ans.append(str(min_val))

def main():
    t = int(input())
    ans = []
    for i in range(t):
        a,b,x,y,n = list(map(int,input().split()))
        solve(a,b,x,y,n,ans)

    print('\n'.join(ans))
    

main()

