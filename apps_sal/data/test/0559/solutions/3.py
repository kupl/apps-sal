p = int(input())
b_list = [0 for _ in range(p-1)]
a_list = list(map(int,input().split()))
def frac(n):
    if a_list[n] == 1:
        t = 1
        for j in range(p-1):
            b_list[j] -= t
            t = (t*n)%p
if a_list[0] == 1:
    b_list[0] -= 1
for i in range(p-1):
    frac(i+1)
b_list.reverse()
print(a_list[0],end = ' ')
for j in b_list:
    print(j % p,end = ' ')

