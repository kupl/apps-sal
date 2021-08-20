ABCD = input()
A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])
if 7 == A + B + C + D:
    print(f'{A}+{B}+{C}+{D}=7')
elif 7 == A + B + C - D:
    print(f'{A}+{B}+{C}-{D}=7')
elif 7 == A + B - C - D:
    print(f'{A}+{B}-{C}-{D}=7')
elif 7 == A - B - C - D:
    print(f'{A}-{B}-{C}-{D}=7')
elif 7 == A + B - C + D:
    print(f'{A}+{B}-{C}+{D}=7')
elif 7 == A - B - C + D:
    print(f'{A}-{B}-{C}+{D}=7')
elif 7 == A - B + C + D:
    print(f'{A}-{B}+{C}+{D}=7')
elif 7 == A - B + C - D:
    print(f'{A}-{B}+{C}-{D}=7')
