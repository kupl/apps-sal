from collections import Counter
n = int(input())
vs = list(map(int, input().split()))

eq_lis = []
odd_lis = []
for i in range(n):
    if i %2 ==0:
        eq_lis.append(vs[i])
    else:
        odd_lis.append(vs[i])
        
a = Counter(eq_lis)
b = Counter(odd_lis)
a_val = list(a.values())
b_val = list(b.values())
a_max = max(a_val)
b_max = max(b_val)

a_sorted = sorted(a.items(), key= lambda x:x[1])
b_sorted = sorted(b.items(), key= lambda x:x[1])

if a_sorted[-1][0] == b_sorted[-1][0]:
    if len(a_sorted) == 1 and len(b_sorted) == 1:
        print(n-a_max)
    elif len(a_sorted)==1 and len(b_sorted) >1:
        print(n-a_max-b_sorted[-2][1])
    elif len(a_sorted)>1 and len(b_sorted) ==1:
        print(n-b_max-a_sorted[-2][1])
    else:
        if b_sorted[-2][1] >= a_sorted[-2][1]:
            print(n-a_max-b_sorted[-2][1])
        else:
            print(n-b_max-a_sorted[-2][1])    
else:
    print(n-a_max-b_max)
