els = "H,He,Li,Be,B,C,N,O,F,Ne,Na,Mg,Al,Si,P,S,Cl,Ar,K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr,Rb,Sr,Y,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe,Cs,Ba,La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu,Hf,Ta,W,Re,Os,Ir,Pt,Au,Hg,Tl,Pb,Bi,Po,At,Rn,Fr,Ra,Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr,Rf,Db,Sg,Bh,Hs,Mt,Ds,Rg,Cn,Nh,Fl,Mc,Lv,Ts,Og"

els = els.upper().split(',')

def check(s):
   for el in els:
      if s == el:
         return True
      match = False
      if len(el) <= len(s):
         match = True
         for x in range(len(el)):
            if s[x] != el[x]:
               match = False
               break
      if match:
         if check(s[len(el):]):
            return True
   return False

print("YES" if check(input()) else "NO")


# __template__
# # input() reads a whole line
# def getarr():
#    return(list(map(int, input().split())))

# def solve():
#    n = input()
#    s = input()
#    print(len(s.replace('UR','D').replace('RU','D')))
   
# # for tc in range(int(input())): solve()

# solve()

