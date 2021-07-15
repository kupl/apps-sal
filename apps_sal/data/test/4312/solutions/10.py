def battle():
    A, B, C, D = map(int, input().split())
    attackT = A // D
    attackA = C // B
    if A % D != 0:
        attackT += 1
    if C % B != 0:
        attackA += 1
    res = "Yes"
    if attackT < attackA:
        res = "No"
        
    print(res)
    
battle()
