word = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    n,a,b = list(map(int,input().split()))
    ans = ''
    sub = word[:b]
    ans+=sub
    for i in range(b,n):
        ans+=(word[i%b])
    print(ans)
