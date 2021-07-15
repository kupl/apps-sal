S =input().replace("H","0")
S = S.replace('D','1')
S_list = list(map(int,S.split()))

if  S_list[0] ^ S_list[1] == 0 :
    result = "H"
else:
    result = "D"
print(result)
