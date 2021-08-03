prvky = """Ac
Ag
Al
Am
Ar
As
At
Au
B
Ba
Be
Bh
Bi
Bk
Br
C
Ca
Cd
Ce
Cf
Cl
Cm
Cn
Co
Cr
Cs
Cu
Db
Ds
Dy
Er
Es
Eu
F
Fe
Fl
Fm
Fr
Ga
Gd
Ge
H
He
Hf
Hg
Ho
Hs
I
In
Ir
K
Kr
La
Li
Lr
Lu
Lv
Md
Mg
Mn
Mo
Mt
N
Na
Nb
Nd
Ne
Ni
No
Np
O
Os
P
Pa
Pb
Pd
Pm
Po
Pr
Pt
Pu
Ra
Rb
Re
Rf
Rg
Rh
Rn
Ru
S
Sb
Sc
Se
Sg
Si
Sm
Sn
Sr
Ta
Tb
Tc
Te
Th
Ti
Tl
Tm
U
Mc
Lv
Ts
Og
V
W
Xe
Y
Yb
Zn
Zr""".split("\n")
d = {i: [] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for i in prvky:
    d[i[0]].append(i)
mem = {}


def f(string):
    if string in mem:
        return mem[string]
    if not string:
        return ""
    for i in d[string[0]]:
        if string.startswith(i.upper()):
            res = f(string[len(i):])
            if res != -1:
                mem[string] = i + res
                return i + res
    return -1


s = input()
r = f(s)
if r == -1:
    print("NO")
else:
    print("YES")
