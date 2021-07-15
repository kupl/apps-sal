A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
L = [(10 - A%10)%10,(10 - B%10)%10,(10 - C%10)%10,(10 - D%10)%10,(10 - E%10)%10]
L.sort()
print(A+B+C+D+E+L[0]+L[1]+L[2]+L[3])
