# cook your dish here
n = 1000000007
x = int(input())
s = ((x + (x**2) % n) % n + (x**3) % n) % n
print(s)
