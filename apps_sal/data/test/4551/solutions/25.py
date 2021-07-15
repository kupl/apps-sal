S = input()
S_list = S.split()

L = int(S_list[0]) + int(S_list[1])
R = int(S_list[2]) + int(S_list[3])
 
if L-R>0:
    print("Left")
elif L-R<0:
    print("Right")
else:
    print("Balanced")
