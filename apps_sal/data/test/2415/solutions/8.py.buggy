#!/bin/python3

import sys

elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

lower = [x.lower() for x in elements]

word = input().lower()

s = ""  # current
t = None  # current + 1
si = -1
ti = None

if word[0] in lower:
    t = elements[lower.index(word[0])] + " "
    ti = 0

while True:
    #	print(s, si, t, ti)
    if si == None and ti == None:
        print("NO")
        return
    if si != None and si == len(word) - 1:
        print("YES")
        return
    if ti != None and ti == len(word) - 1:
        print("YES")
        return
    newT = None
    newTi = None
    newS = t
    newSi = ti
    # get new T
    if ti != None:
        # try advance t by one
        if word[ti + 1] in lower:
            newTi = ti + 1
            newT = t + elements[lower.index(word[ti + 1])] + " "
    if newT == None:  # still none
        # try advance s by 2
        if si != None:
            if word[si + 1:si + 3] in lower:
                newTi = si + 2
                newT = s + elements[lower.index(word[si + 1:si + 3])] + " "
    # get new s
    if newS == None and si != None:
        if word[si + 1] in lower:
            newSi = si + 1
            newS = s + elements[lower.index(word[si + 1])] + " "
    s = newS
    si = newSi
    t = newT
    ti = newTi
