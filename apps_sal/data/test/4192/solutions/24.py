d,t,s = input().strip().split()
d,t,s = [int(d), int(t), int(s)]

sum = d / s

if t >= sum :
  	print('Yes')
else:
    print('No')
