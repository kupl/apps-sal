In = map(str,input().split())
In_list = list(In)
for i in range(len(In_list)):
    In_list[i] = int(In_list[i])
    
ac = In_list[0] * In_list[2]
ad = In_list[0] * In_list[3]
bc = In_list[1] * In_list[2]
bd = In_list[1] * In_list[3]

ans_list = [ac, ad, bc, bd]
ans_list.sort()
print(ans_list[3])
