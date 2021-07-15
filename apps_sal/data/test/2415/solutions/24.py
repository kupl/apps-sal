3

l = ['H', 'HE',
     'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE',
     'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR',
     'K', 'CA', 'SC', 'TI', 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR',
     'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'I', 'XE',
     'CS', 'BA', 'LA', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN',
     'FR', 'RA', 'AC', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG',
     'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU',
     'TH', 'PA', 'U', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR']


def search(s):
    if len(s) == 0:
        return True
    for x in l:
        if s.startswith(x):
            i = len(x)
            if search(s[i:]):
                return True
    return False


s = input()
if search(s):
    print('YES')
else:
    print('NO')

