sum=0
seq=input()
ind=seq.index("^")
for i in range(len(seq)):
    if seq[i].isdigit():
        sum+=(ind-i)*int(seq[i])
if sum==0:
    print("balance")
elif sum>0:
    print("left")
else:
    print("right")
