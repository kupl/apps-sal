a = int(input())
s = input()
ans = a
w_to_r =0
r_to_w =s.count('R')
ans = min(ans,max(w_to_r,r_to_w))
for i in range(a):
    if s[i] =='W':
        w_to_r +=1
    else:
        r_to_w -=1
    ans = min(ans,max(w_to_r,r_to_w))
print(ans)       
