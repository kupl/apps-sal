a = ['H','HE','LI','BE','B','C','N','O','F','NE','NA','MG','AL','SI','P','S','CL','AR','K','CA','SC','TI','V','CR','MN','FE','CO','NI','CU','ZN','GA','GE','AS','SE','BR','KR','RB','SR','Y','ZR','NB','MO','TC','RU','RH','PD','AG','CD','IN','SN','SB','TE','I','XE','CS','BA','LA','CE','PR','ND','PM','SM','EU','GD','TB','DY','HO','ER','TM','YB','LU','HF','TA','W','RE','OS','IR','PT','AU','HG','TL','PB','BI','PO','AT','RN','FR','RA','AC','TH','PA','U','NP','PU','AM','CM','BK','CF','ES','FM','MD','NO','LR','RF','DB','SG','BH','HS','MT','DS','RG','CN','NH','FL','MC','LV','TS','OG']

def check(s):
    if len(s) == 0:
        return 'YES'
    elif len(s) == 1:
        if s in a:
            return 'YES'
        else:
            return 'NO'
    else:
        s1 = ''
        s2 = ''
        if s[:1] in a:
            s1 = check(s[1:])
        if s[:2] in a:
            s2 = check(s[2:])
        if s1 == 'YES' or s2 == 'YES':
            return 'YES'
        else:
            return 'NO'

import sys
for line in sys.stdin:
    print(check(line[:-1]))
