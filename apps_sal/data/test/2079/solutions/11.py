n = int(input())
w=list(map(int, input().split()))
a=sorted(list(range(1,n+1)),key=lambda i:w[i-1])
i,s,o=0,[],[]
for c in input():
    if c=='0':
        o.append(a[i])
        s.append(a[i])
        i+=1
    else:
        o.append(s.pop())
print(*o)

