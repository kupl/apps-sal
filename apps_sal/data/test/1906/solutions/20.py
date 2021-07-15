incl = [2, 3, 5, 7, 30, 42, 70, 105]
excl = [6, 10, 14, 15, 21, 35, 210]

n = int(input())
answ = 0

for k in incl:
    answ += n // k
    
for k in excl:
    answ -= n // k
    
print(n-answ)
