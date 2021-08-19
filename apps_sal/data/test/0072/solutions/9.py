n = int(input())
(ku, sh, ka) = (input(), input(), input())
(l_ku, l_sh, l_ka) = (max([ku.count(i) for i in list(set(ku))]), max([sh.count(i) for i in list(set(sh))]), max([ka.count(i) for i in list(set(ka))]))
if len(ku) - l_ku > n:
    l_ku += n
elif l_ku == len(ku) and n == 1:
    l_ku -= 1
else:
    l_ku = len(ku)
if len(sh) - l_sh > n:
    l_sh += n
elif l_sh == len(sh) and n == 1:
    l_sh -= 1
else:
    l_sh = len(sh)
if len(ka) - l_ka > n:
    l_ka += n
elif l_ka == len(ka) and n == 1:
    l_ka -= 1
else:
    l_ka = len(ka)
ma = max([l_sh, l_ku, l_ka])
if l_ka == l_sh and l_ka == ma or (l_ku == l_sh and l_ku == ma) or (l_ka == l_ku and l_ka == ma):
    print('Draw')
elif ma == l_ka:
    print('Katie')
elif ma == l_sh:
    print('Shiro')
elif ma == l_ku:
    print('Kuro')
