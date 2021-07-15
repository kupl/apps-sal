n=int(input())
w=list(input() for i in range(n))
a=[w[0]]
for j in range(1,n):
    if w[j] not in a and w[j][0]==a[j-1][-1]:
        a.append(w[j])
        continue
    else:
        print("No")
        break
else:
    print("Yes")
