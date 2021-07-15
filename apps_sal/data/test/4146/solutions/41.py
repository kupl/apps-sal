def find_max( list ):
    x = 0
    x2 = 0
    x_i = 0
    x2_i = 0
    for i in range( len(list) ):
        if x < list[i]:
            x = list[i]
            x_i = i
    for i in range( len(list) ):
        if i == x_i:
            continue
        if x2 < list[i] <= x:
            x2 = list[i]
            x2_i = i
    return x,x2,x_i,x2_i

n = int( input() )
v = list ( int(x) for x in input().split() )

v_sort = sorted( v )

v_odd = [ 0 for i in range( v_sort[-1] + 1 ) ]
#奇数
v_eve = [ 0 for i in range( v_sort[-1] + 1 ) ]
#偶数
for i in range( n ):
    if i % 2 == 0:
        v_eve[ v[i] ] += 1
    if i % 2 == 1:
        v_odd[ v[i] ] += 1

vex,vex2,vex_i,vex2_i = find_max( v_eve )
vox,vox2,vox_i,vox2_i = find_max( v_odd )

ok = 0
# ok: figure that need not to fix
if vex_i != vox_i:
    ok = vex + vox
else:
    ok = max( vex + vox2 , vex2 + vox )

ans = n - ok
print( ans )
