D,G = map(int,input().split())
dic1 = {}
dic2 = {}
dic3 = []
min_ans = 10000000000
#dicはdic[点数][問題数][コンプリート]
for i in range(1,D+1):
    p,c = map(int,input().split())
    dic1[i*100] = p
    dic2[i*100] = i*100*p+c
    dic3.append(i*100)

n = len(dic1)
for i in range(2 ** n):
    bag = []
    bag_sum = 0
    bag_len = 0
    for j in range(n):
        if ((i >> j) & 1):
            bag.append(dic3[j])
    for k in range(len(bag)):
        bag_sum += dic2[bag[k]]
        bag_len += dic1[bag[k]]

    if bag_sum >= G:
        min_ans = min(min_ans,bag_len)
    else:
        for i in range(len(dic3)):
            if dic3[(i+1)*-1] in bag:
                continue
            for u in range(dic1[dic3[(i+1)*-1]]-1):
                bag_len += 1
                bag_sum+=dic3[(i+1)*-1]
                if bag_sum >= G:

                    min_ans = min(min_ans,bag_len)
                    break

    
print(min_ans)
