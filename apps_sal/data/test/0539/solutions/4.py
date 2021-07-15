# Imports


##############################################
# Input
n = int(input())

##############################################
# Main code
res = 0
for a in range(1, n+1):
    for b in range(a, n+1):
        c = a ^ b
        if c <= n and c >= b and c < (a+b) and a > (c-b) and b > (c-a):
            res += 1

print(res)








