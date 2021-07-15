from sys import stdin, stdout
def rsingle_int():
    return int(stdin.readline().rstrip())
 
def rmult_int():
    return [ int(x) for x in stdin.readline().rstrip().split() ]
 
def r_str():
    return stdin.readline().rstrip()
    
def rsingle_char():
    return stdin.read(1)
 
def main():
    s, b = rmult_int()
    a = rmult_int()

    a_order = a.copy()
    a.sort()

    a_g = {}
    for el in a:
        a_g[el] = 0

    ds = []
    d_g = {}
    for i in range(b):
        d, g = rmult_int()
        if d in d_g:
            d_g[d] += g
        else:
            d_g[d] = g
            ds.append(d)

    ds.sort()
    ds_len = len(ds)
    
    acc = 0
    d_i = 0
    for el in a:
        while d_i < ds_len and ds[d_i] <= el:
            acc += d_g[ds[d_i]]
            d_i += 1
        a_g[el] = acc
    
    out = []
    for el in a_order:
        out.append(int(a_g[el]))
    print(*out)

 
main()
