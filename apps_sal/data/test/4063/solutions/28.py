n = int(input())
d_l = list(map(int, input().split()))
d_l = sorted(d_l)
if len(d_l) %2 != 0:
    print(0)
else:
    idx = int(len(d_l)/2)
    abc = d_l[idx-1]
    agc = d_l[idx]
    print(agc-abc)
