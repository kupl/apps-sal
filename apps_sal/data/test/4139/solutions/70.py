import itertools

N = input()

if len(N)<=2:
    print((0))
    return
product_list = []
for i in range(3,len(N)+1):
    product_list += list(itertools.product('753',repeat=i))
#print(product_list)
res = 0

for i in product_list:
    num = ''.join(list(i))
    if int(N) < int(num):
        continue
    if num.count('5')>0 and num.count('7')>0 and num.count('3')>0:
        res += 1
print(res)

