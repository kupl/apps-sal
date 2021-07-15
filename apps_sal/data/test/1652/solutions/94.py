S=input()
T=""
l=["maerd","remaerd","esare","resare"]
flag=True
for i in range(len(S)):
    T=T+S[len(S)-1-i]
    if T in l:
        T=""
    if len(T)>7:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")
