s1 = input()
ls = input().split()
print('YES' if any(any(s1[i] == ls[j][i] for i in range(2)) for j in range(5)) else 'NO')
