# written by sak
#
#	sk<3
#
# powered by codechef

n = int(input())
change = 0
ordered = 1
p = 997979
q = 86949
while n > 0:
    x = input()
    x = x.split(' ')
    if(int(x[0]) > p):
        ordered = 0
    p = int(x[0])
    q = int(x[1])
    if(p != q):
        change = 1
    n -= 1

if(change == 1):
    print("rated")
elif(ordered == 0):
    print("unrated")
else:
    print("maybe")
