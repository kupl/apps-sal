from itertools import permutations
n = int(input())
p = input().replace(" ","")
q = input().replace(" ","")

c = permutations([i for i in range(1,n+1)],n)
for i,a in enumerate(c):
    num = "".join(map(str,a))
    # print(num)
    if p==num:pi=i+1
    if q==num:qi=i+1
print(abs(pi-qi))
