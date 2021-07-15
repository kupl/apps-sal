#Zad
from collections import Counter
n=int(input())
tree=[]
for i in range(n-1):
    tree.extend(list(map(int,input().split())))
ans=Counter(tree)
if ans.most_common(2)[1][1]>2: print('No')
else:
    print('Yes')
    if n==2:
        print(1)
        print('1 2')
    else:
        if ans.most_common(1)[0][1]==2:
            print(1)
            print(ans.most_common()[-2][0], ans.most_common()[-1][0])
        else:
            center=ans.most_common(1)[0][0]
            kraya=[n[0] for n in ans.most_common() if n[1]==1]
            print(len(kraya))
            for i in kraya:
                print(center, i)
