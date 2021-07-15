n=int(input())
l=[]
for i in input().split():
    tmp=1&int(i)
    if l==[] or l[-1]!=tmp: l.append(tmp)
    else: l.pop()

print("YES" if len(l)<2 else "NO")
