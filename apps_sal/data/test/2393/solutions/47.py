t = int(input())
for i in range(t):
    s = input()
    sy = 0
    A = set()
    for j in range(len(s)-2):
        if s[j] + s[j+1] + s[j+2] == 'one':
            if s[j-1] == 'o':
                A.add(j+1)
            else:
                A.add(j)
        elif s[j] + s[j+1] + s[j+2] == 'two':
            if j < len(s) - 3 and s[j+3] == 'o':
                A.add(j+1)
            else:
                A.add(j+2)
    print(len(A))
    for j in A:
        print(j+1, end= ' ')
    print()
    
