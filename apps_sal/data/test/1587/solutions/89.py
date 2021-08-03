N = int(input())
C = list(input())

R_count = C.count('R')
if R_count == 0:
    print((0))
    return

C_count = C[:R_count].count('R')
print((R_count - C_count))
