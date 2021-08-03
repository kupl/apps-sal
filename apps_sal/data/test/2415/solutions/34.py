a = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "Hf", "Ta", "W", "Re",
     "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]


def f(x):
    n = len(a)
    for i in range(n):
        if (a[i] == x):
            return 1
    return 0


def dfs(cur, s, n):
    if (cur >= n):
        return 1
    flg = 0
    if (cur < n - 1):
        if (f(str() + s[cur] + s[cur + 1]) == 1):
            flg |= dfs(cur + 2, s, n)
    if (f(s[cur]) == 1):
        flg |= dfs(cur + 1, s, n)
    return flg


n = len(a)
for i in range(n):
    a[i] = a[i].upper()
s = list(input())
n = len(s)
i = 0
flg = dfs(0, s, n)
if (flg == 0):
    print("NO")
else:
    print("YES")
