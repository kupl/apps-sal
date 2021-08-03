
def max(a, b):
    if(a >= b):
        return a
    else:
        return b

####################################


s = input().split()
length = len(s)
n = int(s[length - 1])

plus = 1
minus = 0


for i in s:
    if(i == '+'):
        plus += 1
    if(i == '-'):
        minus += 1

if(plus * n - minus < n or plus - n * minus > n):
    print('Impossible')
    return
else:
    print('Possible')

for i in range(0, length - 1, 2):  # initializing all placeholders with 1
    s[i] = '1'


# if(minus==0):
# 	s[0]= repr(n-plus+1)

# else:


# 	diff=plus-1-minus


# 	if(diff>0):
# 		s[0]=repr(n-diff)
# 		for i in range(2, length-1, 2):
# 			s[i]='1'

# 	flag=0
# 	if(diff<=0):
# 		s[0]=repr(n)
# 		for i in range(2, length-1, 2):
# 			s[i]='1'
# 			if(flag==0 and s[i-1] == '+'):
# 				flag=1
# 				s[i]=repr(1-diff)

res = n - plus + minus
for i in range(0, length - 1, 2):
    if((i == 0 or s[i - 1] == '+') and res > 0):
        val = int(s[i])
        if(res > n - val):
            res -= (n - val)
            s[i] = repr(n)
        else:
            val += res
            s[i] = repr(val)
            res = 0
    elif(s[i - 1] == '-' and res < 0):
        val = int(s[i])
        if(res < val - n):
            res += (n - val)
            s[i] = repr(n)
        else:
            val -= res
            s[i] = repr(val)
            res = 0


print(' '.join(s))
