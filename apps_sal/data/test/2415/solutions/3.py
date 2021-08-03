table = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og Uue Ubn Ubu Ubb Ubt Ubq Ubp Ubh Ubs"
elements = [x.upper() for x in table.split()]


def elementary(word):
    if word == "":
        return True
    if word[0:1] in elements and elementary(word[1:]):
        return True
    if word[0:2] in elements and elementary(word[2:]):
        return True
    if word[0:3] in elements and elementary(word[3:]):
        return True
    return False


word = input()
if elementary(word):
    print("YES")
else:
    print("NO")
