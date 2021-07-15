a, b = list(map(int,input().split()))

my_list = []

if a > b:
    for i in range(a):
        my_list.append(b)
elif b > a:
    for i in range(b):
        my_list.append(a)
else:
    for i in range(a):
        my_list.append(b)
        
print(''.join([str(n) for n in my_list]))
