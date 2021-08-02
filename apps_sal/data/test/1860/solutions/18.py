n = int(input())
s = 0
while(n >= 1):
    s += 2**n
    n -= 1
print(s)
