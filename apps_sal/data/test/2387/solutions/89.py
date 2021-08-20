N = int(input())
C_p = []
C_m = []
for i in range(N):
    kakko = input()
    temp = 0
    temp_min = 0
    for s in kakko:
        if s == '(':
            temp += 1
        else:
            temp -= 1
            temp_min = min(temp, temp_min)
    if temp >= 0:
        C_p.append((temp_min, temp))
    else:
        C_m.append((temp_min - temp, temp_min, temp))
C_p.sort(reverse=True)
flag = 0
final = 0
for (l, f) in C_p:
    if final + l < 0:
        flag = 1
    final += f
C_m.sort()
for (_, l, f) in C_m:
    if final + l < 0:
        flag = 1
    final += f
if final != 0:
    flag = 1
print('Yes' if flag == 0 else 'No')
