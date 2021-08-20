ele = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar,A', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
for i in range(len(ele)):
    if len(ele[i]) == 2:
        ele[i] = ele[i][0] + chr(ord(ele[i][1]) - 32)
ele = ['AC', 'AG', 'AL', 'AM', 'AR', 'AS', 'AT', 'AU', 'B', 'BA', 'BE', 'BH', 'BI', 'BK', 'BR', 'C', 'CA', 'CD', 'CE', 'CF', 'CL', 'CM', 'CN', 'CO', 'CR', 'CS', 'CU', 'DB', 'DS', 'DY', 'ER', 'ES', 'EU', 'F', 'FE', 'FL', 'FM', 'FR', 'GA', 'GD', 'GE', 'H', 'HE', 'HF', 'HG', 'HO', 'HS', 'I', 'IN', 'IR', 'K', 'KR', 'LA', 'LI', 'LR', 'LU', 'LV', 'MC', 'MD', 'MG', 'MN', 'MO', 'MT', 'N', 'NA', 'NB', 'ND', 'NE', 'NH', 'NI', 'NO', 'NP', 'O', 'OG', 'OS', 'P', 'PA', 'PB', 'PD', 'PM', 'PO', 'PR', 'PT', 'PU', 'RA', 'RB', 'RE', 'RF', 'RG', 'RH', 'RN', 'RU', 'S', 'SB', 'SC', 'SE', 'SG', 'SI', 'SM', 'SN', 'SR', 'TA', 'TB', 'TC', 'TE', 'TH', 'TI', 'TL', 'TM', 'TS', 'U', 'V', 'W', 'XE', 'Y', 'YB', 'ZN', 'ZR']
s = input().strip()
d = [False] * len(s) * 2
d[0] = True
for i in range(len(s)):
    if d[i]:
        if s[i] > 'Z':
            while True:
                s += '1'
        for e in ele:
            if s[i] == e:
                d[i + 1] = True
            elif s[i:i + 2] == e:
                d[i + 2] = True
if d[len(s)]:
    print('YES')
else:
    print('NO')
