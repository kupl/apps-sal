a = input()
b = input()
q = 0
for i in range(-1,-min(len(a),len(b))-1,-1):
    if a[i] != b[i]:
        break
    q+=1
print(len(a) + len(b) - 2*q)

