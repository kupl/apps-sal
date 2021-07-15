q=int(input())
for i in range(q):
    ok=[x for x in input().split()]
    r=ok[0]
    s=ok[1]
    w = [(ord(r[i])) for i in range(len(r))]
    w.sort()
    w=[chr(w[i]) for i in range(len(r))]
    first=True
    at=-1
    for j in range(len(r)):
        if w[j]!=r[j]:
            first=False
            at=j
            break
    if first==False:
        t=r[::-1].find(w[at])
        r=r[:at]+w[at]+r[at+1:len(r)-1-t]+r[at]+r[len(r)-t:]
    if r<s:
        print(r)
    else:
        print("---")
