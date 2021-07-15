from collections import Counter
n = int(input())
a = input()[:n]
b = input()[:n]
prelim =0
for i in range(n//2):
    c = Counter([a[i],a[n-1-i],b[i],b[n-1-i]])
    k = len(c)
    if k == 4:
        """
        a x +2op
        b y
        """
        prelim +=2
    elif k == 3:
        """
        a c  +1op
        a b
        
        a a  +2op
        b c
        
        a c  +1op
        b b
        """
        prelim += 2 if a[i]==a[n-1-i] else 1
    elif k==2:
        """
        3 3
        3 5
        
        3 5
        3 3
        
        2 5
        2 5
        """
        if 3 in list(c.values()):
            prelim += 1
if n%2:
    if a[n//2]!=b[n//2]:
        prelim +=1

print(prelim)




