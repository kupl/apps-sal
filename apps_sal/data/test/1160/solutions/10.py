def solve(a, n):
    M={'S':0, 'M':1, 'L':2, 'XL':3, 'XXL':4, 'XXXL':5}
    m={0:'S', 1:'M', 2:'L', 3:'XL', 4:'XXL', 5:'XXXL'}
    p=[ [] for _ in range(5) ]
    ans=['']*n
    for i in range(n):
        s=input()
        if ',' in s:
            p[ M[ s[:s.find(',')] ] ]+=[i]
        else:
            s=M[s]
            if a[s]<=0:
                return []
            a[s]-=1
            ans[i]=m[s]
    for i in range(5):
        for x in p[i]:
            if a[i]>0:
                a[i]-=1
                ans[x]=m[i]
            elif a[i+1]>0:
                a[i+1]-=1
                ans[x]=m[i+1]
            else:
                return []
    return ans
ans=solve(list(map(int, input().split())), int(input()))
if ans==[]:
    print('NO')
else:
    print('YES')
    for s in ans:
        print(s)
