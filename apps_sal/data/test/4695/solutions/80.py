print('YNeos'[len(set([0 if i==2 else [1,2][i in [4,6,9,11]] for i in list(map(int,input().split()))]))!=1::2])
