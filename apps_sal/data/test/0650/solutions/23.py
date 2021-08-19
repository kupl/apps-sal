s = input()
a = {'A', 'E', 'F', 'H', 'I', 'K', 'L', 'M', 'N', 'T', 'V', 'W', 'X', 'Y', 'Z'}
b = {'B', 'C', 'D', 'G', 'J', 'O', 'P', 'Q', 'R', 'S', 'U'}
print('YES' if all((c in a for c in s)) or all((c in b for c in s)) else 'NO')
