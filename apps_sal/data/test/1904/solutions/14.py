lens = int(input())
res_h, res_a, res_r, res_d = 0, 0, 0, 0
for ch, amb in zip(input(), [int(x) for x in input().split()]):
    if    ch == "h": res_h += amb
    elif  ch == "a": res_a  = min(res_a + amb, res_h)
    elif  ch == "r": res_r  = min(res_r + amb, res_a)
    elif  ch == "d": res_d  = min(res_d + amb, res_r)
print(res_d)

