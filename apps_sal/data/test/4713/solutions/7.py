n=int(input())
s=input()
x=[0]
for i in s:
    if i=="I":
        x.append(x[-1]+1)
    else:
        x.append(x[-1]-1)
print(max(x))
