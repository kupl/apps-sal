sa=input().split(' ')
rs=int(sa[0])
k=int(sa[1])
joy=-99999999999999999999999999999999999
for x in range(rs):
    sa2=input().split(' ')
    f_i=int(sa2[0])
    t_i=int(sa2[1])
    if t_i>k:
        joy=max(joy, f_i-(t_i-k))
    else:
        joy=max(joy, f_i)
print(joy)

