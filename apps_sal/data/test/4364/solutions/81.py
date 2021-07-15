s = input()
def YYMM(s):
    p = int(s[2:])
    if 1 <= p <= 12:
        return True
    return False

def MMYY(s):
    p = int(s[:2])
    if 1 <= p <= 12:
        return True 
    return False

if YYMM(s) and MMYY(s):
    print('AMBIGUOUS')
elif YYMM(s):
    print('YYMM')
elif MMYY(s):
    print('MMYY')
else:
    print('NA')
