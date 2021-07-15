n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

num_list = [a,b,c,d,e]

if n % min(num_list) == 0:
    print(4 + n //min(num_list))
else:
    print(5 + n // min(num_list))
