a=['AC','RF','DB','SG','BH','HS','MT','DS','RG','CN','NH','FL','MC','TS','OG','LV', 'AL', 'AM', 'SB', 'AR', 'AS', 'AT', 'BA', 'BK', 'BE', 'BI', 'B', 'BR', 'CD', 'CA', 'CF', 'C', 'CE', 'CS', 'CL', 'CR', 'CO', 'CU', 'CM', 'DY', 'ES', 'ER', 'EU', 'FM', 'F', 'FR', 'GD', 'GA', 'GE', 'AU', 'HF', 'HE', 'HO', 'H', 'IN', 'I', 'IR', 'FE', 'KR', 'LA', 'LR', 'PB', 'LI', 'LU', 'MG', 'MN', 'MD', 'HG', 'MO', 'ND', 'NE', 'NP', 'NI', 'NB', 'N', 'NO', 'OS', 'O', 'PD', 'P', 'PT', 'PU', 'PO', 'K', 'PR', 'PM', 'PA', 'RA', 'RN', 'RE', 'RH', 'RB', 'RU', 'SM', 'SC', 'SE', 'SI', 'AG', 'NA', 'SR', 'S', 'TA', 'TC', 'TE', 'TB', 'TL', 'TH', 'TM', 'SN', 'TI', 'W', 'U', 'V', 'XE', 'YB', 'Y', 'ZN', 'ZR']
a=set(a)
x=input()
ok=[False]*len(x)
for i in range(len(x)):
    if x[i] in a:
        ok[i]=True

for i in range(len(x)-1):
    if x[i:i+2] in a:
        ok[i]=True
        ok[i+1]=True
print('YES' if all(ok) else 'NO')
