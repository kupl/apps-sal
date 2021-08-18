

S = input()
T = input()


mydict = {}
for i in range(len(S)):
    if S[i] in mydict:
        if T[i] != mydict[S[i]]:
            ans = "No"
            break
    else:
        mydict[S[i]] = T[i]
else:
    a = list(mydict.values())
    b = list(set(a))
    if len(b) != len(a):
        ans = "No"
    else:
        ans = "Yes"
print(ans)
