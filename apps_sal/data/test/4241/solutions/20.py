a = [str(input()) for i in range(2)]
S = a[0]
T = a[1]
length_S = len(S)
length_T = len(T)
l_S = [str(x) for x in list(str(S))]
l_T = [str(y) for y in list(str(T))]
l_s = []
for i in range(length_S - length_T + 1):
    s = l_S[i:i + length_T]
    l_s.append(s)
l_b = []
for j in range(length_S - length_T + 1):
    l_a = []
    num1 = 0
    for i in range(length_T):
        if l_T[i] != l_s[j][i]:
            num1 += 1
        l_a.append(num1)
    l_b.append(l_a)
l_c = []
for i in range(length_S - length_T + 1):
    num2 = l_b[i][-1]
    l_c.append(num2)
ans = min(l_c)
print(ans)
