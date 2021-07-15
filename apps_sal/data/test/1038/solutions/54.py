n,m = map(int, input().split())

if m ==0:
    print(0)
    return

nl = m.bit_length()
temp = ["0"]*nl

res= [2,3]
ress = [1,2]
res_ju =0
ress_ju =0

if n % 4 in res:
    res_ju = 1
if m % 4 in ress:
    ress_ju = 1
if res_ju ^ ress_ju ==1:
    temp[nl-1]="1"

mod = 4
for i in range(2,nl+1):
    mod *= 2
    res_ju =0
    ress_ju =0
    nn = n% mod
    mm = m% mod
    if nn % 2==1 and nn % (mod//2) >(mod//4):
        res_ju = 1
    if mm % 2 ==0 and mm % (mod//2)+1 > (mod//4):
        ress_ju = 1
    if res_ju ^ ress_ju ==1:
        temp[nl-i]="1"

result = (''.join(temp))

print(int(result,2))
