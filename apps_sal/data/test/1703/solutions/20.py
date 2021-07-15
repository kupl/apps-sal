def transform(seq):
    st = []
    for i in range(len(seq)):
        if (len(st) > 0):
            if (st[-1] == '(' and seq[i] == ')'):
                st.pop()
            else:
                st.append(seq[i])
        else:
            st.append(seq[i])
    return "".join(st)
    
n = int(input())

brs = dict()
for i in range(n):
    br = transform(input())    
    if (br in brs.keys()):
        brs[br] += 1
    else: 
        brs[br] = 1
ans = 0  
for br_l in brs.keys():
    for br_r in brs.keys():
        br = br_l + br_r
        if (len(br_l) == len(br_r)):
            if (transform(br) == ""):                
                #brs.pop(br_l)
                if (br_l == br_r):
                    ans += (brs[br_l] * (brs[br_l] - 1)  + brs[br_l])
                else:
                    ans += brs[br_l] * brs[br_r]    
                    #brs.pop(br_r)
                break
print(int(ans))
