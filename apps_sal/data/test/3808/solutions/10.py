len = int(input())
s = input()

st = neg = 0
for i in s:
    if i == '(':
        st += 1
    else:
        st -= 1
    
    neg = min(neg, st)

if st != 0 or neg < -1:
    print("No")
else:
    print("Yes")
