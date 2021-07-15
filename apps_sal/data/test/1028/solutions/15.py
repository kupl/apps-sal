import sys
f = sys.stdin
#f = open('H:\\Portable Python 3.2.5.1\\test_248B1.txt') 

n, m = map(int, f.readline().strip().split())

k_max = (n-(m-1))*(n-(m-1) - 1)//2

n1 = n // m
n2 = n1 + 1
m2 = n % m 
m1 = m - m2

k_min = m1*(n1)*(n1 - 1) // 2 + m2*(n2)*(n2 - 1) // 2

print(str(k_min) + ' ' + str(k_max))
