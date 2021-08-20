e = ['AC', 'AG', 'AL', 'AM', 'AR', 'AS', 'AT', 'AU', 'B', 'BA', 'BE', 'BH', 'BI', 'BK', 'BR', 'C', 'CA', 'CD', 'CE', 'CF', 'CL', 'CM', 'CN', 'CO', 'CR', 'CS', 'CU', 'DB', 'DS', 'DY', 'ER', 'ES', 'EU', 'F', 'FE', 'FL', 'FM', 'FR', 'GA', 'GD', 'GE', 'H', 'HE', 'HF', 'HG', 'HO', 'HS', 'I', 'IN', 'IR', 'K', 'KR', 'LA', 'LI', 'LR', 'LU', 'LV', 'MC', 'MD', 'MG', 'MN', 'MO', 'MT', 'N', 'NA', 'NB', 'ND', 'NE', 'NH', 'NI', 'NO', 'NP', 'O', 'OG', 'OS', 'P', 'PA', 'PB', 'PD', 'PM', 'PO', 'PR', 'PT', 'PU', 'RA', 'RB', 'RE', 'RF', 'RG', 'RH', 'RN', 'RU', 'S', 'SB', 'SC', 'SE', 'SG', 'SI', 'SM', 'SN', 'SR', 'TA', 'TB', 'TC', 'TE', 'TH', 'TI', 'TL', 'TM', 'TS', 'U', 'V', 'W', 'XE', 'Y', 'YB', 'ZN', 'ZR']
s = input()
dp = [0] * (len(s) + 1)
dp[0] = 1
for i in range(1, len(s) + 1):
    for ei in e:
        if len(ei) <= i and ei == s[i - len(ei):i] and (dp[i - len(ei)] == 1):
            dp[i] = 1
print('YES' if dp[len(s)] else 'NO')
