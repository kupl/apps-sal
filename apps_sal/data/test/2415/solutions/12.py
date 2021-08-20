elems = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE', 'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K', 'CA', 'SC', 'TI', 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'U', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']
s = str(input())
cando = [False] * len(s)
good = False
for elem in elems:
    if s.startswith(elem):
        cando[len(elem) - 1] = True
for i in range(1, len(s)):
    for elem in elems:
        ln = len(elem)
        if ln > i + 1:
            continue
        substr = s[i + 1 - ln:i + 1]
        if substr == elem:
            cando[i] = cando[i] or cando[i - ln]
if cando[len(s) - 1]:
    print('YES')
else:
    print('NO')
'\nwith open(\'elements.txt\', \'r\') as e:\n    ele = e.read()\n    \nele = ele.split(\'\n\')\n\nelements = []\n\nfor elem in ele:\n    if len(elem) > 0:\n        parts = elem.split(\'-\')\n        element = parts[0].strip()\n        elements.append(element)\n        \nres = \'[\'\nfor elem in elements:\n    res = res + "\'" + elem.upper() + "\',"\nres = res[:-1]\nres += \']\'\n\nprint(res)\n'
