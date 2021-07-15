import itertools,bisect

num_list = []#753数となりえる数の生成
for i in range(3,10):
    num_list += list(itertools.product('753',repeat=i) )
    
num = []#753数の絞り込み
for nm in num_list:
    if '3' in nm and '5' in nm and '7' in nm:
        num.append(int(''.join(nm)))

num.sort()#にぶたん
print((bisect.bisect_right(num,int(input()))))

