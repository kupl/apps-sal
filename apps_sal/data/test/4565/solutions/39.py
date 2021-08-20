n = int(input())
s = input()
e_all = s.count('E')
w_all = s.count('W')
e_l = 0
w_l = 0
unti = [0] * n
for i in range(n):
    if s[i] == 'E':
        e_l += 1
        unti[i] = w_l + (e_all - e_l)
    if s[i] == 'W':
        unti[i] = w_l + (e_all - e_l)
        w_l += 1
print(min(unti))
