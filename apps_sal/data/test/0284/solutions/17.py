n = int(input())

def tre(n):
    if n % 1234 == 0:
        return True
    return False

def dva(n):
    if n % 123456 == 0:
        return True
    else:
        k = n // 123456
        nn = n - k*123456
        for i in range (k, -1, -1):
            if tre(nn):
                return True
            nn += 123456
        return False

def one(n):
    if n % 1234567 == 0:
        return True
    else:
        kk = n // 1234567
        nnn = n - kk*1234567
        for i in range (kk, -1, -1):
            if dva(nnn):
                return True
            nnn += 1234567
        return False           


if n < 1234:
    print('NO')
elif n < 123456:
    if tre(n):
        print('YES')
    else:
        print('NO')
elif n < 1234567:
    if dva(n):
        print('YES')
    else:
        print('NO')
else:
    if one(n):
        print('YES')
    else:
        print('NO')
    
    
    

