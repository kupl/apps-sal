strs = """Ac
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
Mc
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
Nh
Ni
No
Np
O
Og
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
Ts
U
Ubb
Ubh
Ubn
Ubp
Ubq
Ubt
Ubu
Uue
V
W
Xe
Y
Yb
Zn
Zr"""
ele = strs.upper().split("\n")
inp = input()
n = len(inp)
dp = [False] * (n + 1)
dp[0] = True
for i in range(1, n + 1):
    if dp[i - 1] == True and inp[i - 1:i] in ele:
        dp[i] = True
    elif i > 1 and dp[i - 2] == True and inp[i - 2:i] in ele:
        dp[i] = True
    elif i > 2 and dp[i - 3] == True and inp[i - 3:i] in ele:
        dp[i] = True

if dp[n]:
    print("YES")
else:
    print("NO")
