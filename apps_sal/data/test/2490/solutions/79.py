#E
#greedy 
n = input()
l = len(n)

#a is kuriagari naku, pittari na case
#b is kuriagari ari
a,b = 0,1
for v in n:
    v = int(v)
    a_next = min(a+v, b+(10-v))
    b_next = min(a+v+1, b+(10-(v+1)))
    a = a_next
    b = b_next
    
    #繰り上がりが発生する⇔引く数を+1する
    #(10-v)や(10-(v+1)) means charges
    #last keta is pittari, no amari happenes

print(a)
