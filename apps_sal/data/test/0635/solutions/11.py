n, s = [int(x) for x in input().split()]
lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

if lst1[0]==1 and lst1[s-1]==1:
        print("YES")
        return
elif lst1[0]==0 or (lst1[s-1]==0 and lst2[s-1]==0):
        print("NO")
        return
for i in range(s,n):
        if (lst1[i]==1 and lst2[i]==1):
                print("YES")
                return
print("NO")

