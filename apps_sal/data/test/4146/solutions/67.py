n=int(input())
a=[int(i) for i in input().split()]

one=[]
two=[]

for i in range(n):
    if i%2==0:
        one.append(a[i])
    else:
        two.append(a[i])

one_count=[0]*(10**5+1)
two_count=[0]*(10**5+1)

for i in one:
    one_count[i]+=1
for i in two:
    two_count[i]+=1

one_first_index=0
one_max_count=0
for i,value in enumerate(one_count):
    if one_max_count<value:
        one_max_count=value
        one_first_index=i
one_second_index=0
one_second_max_count=0
for i,value in enumerate(one_count):
    if one_second_max_count<value and i!=one_first_index:
        one_second_max_count=value
        one_second_index=i

two_first_index=0
two_max_count=0
for i,value in enumerate(two_count):
    if two_max_count<value:
        two_max_count=value
        two_first_index=i
two_second_index=0
two_second_max_count=0
for i,value in enumerate(two_count):
    if two_second_max_count<value and i!=two_first_index:
        two_second_max_count=value
        two_second_index=i



if one_first_index!=two_first_index:
    print((n-one_max_count-two_max_count))
elif one_max_count-one_second_max_count<=two_max_count-two_second_max_count:
    print((n - one_second_max_count - two_max_count))
else:
    print((n - two_second_max_count - one_max_count))




