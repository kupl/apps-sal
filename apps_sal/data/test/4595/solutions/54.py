s = input()
ind_A = 0
while s[ind_A] != 'A':
    ind_A += 1
ind_Z = len(s)
while s[ind_Z - 1] != 'Z':
    ind_Z -= 1
print(ind_Z - ind_A)
