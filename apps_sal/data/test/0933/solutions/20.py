s=input()
res=""

for ch in s:
    ok=True
    if len(res)>=2:
        if ch==res[-1] and res[-1]==res[-2]:
            ok=False

    if len(res)>=3:
        if ch==res[-1] and res[-2]==res[-3]:
            ok=False
    if ok:
        res+=ch

print(res)


