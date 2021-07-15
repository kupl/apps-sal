n=int(input())
word=[]
val=[]
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(n):
    a=input()
    if len(set(a))>2:
        pass
    else:
        word.append(set(a))
        val.append(len(a))
m=0
for i in alpha:
    for j in alpha:
        s=0
        for k in range(len(word)):
            if word[k].issubset({i,j}):
                s+=val[k]
        m=max(m,s)
print(m)
