a = [0] * 4
for i in range(4):
    a[i] = input()
t = False
for i in range(4):
    q1 = [a[0][i], a[1][i], a[2][i]]
    q2 = [a[1][i], a[2][i], a[3][i]]
    if (q1.count("x") == 2 and q1.count(".") == 1) or (q2.count("x") == 2 and q2.count(".") == 1):
        t = True  
for i in range(4):
    q3 = [a[i][0], a[i][1], a[i][2]]
    q4 = [a[i][1], a[i][2], a[i][3]]    
    if (q3.count("x") == 2 and q3.count(".") == 1) or (q4.count("x") == 2 and q4.count(".") == 1):
        t = True    
q1 = [a[0][1], a[1][2], a[2][3]]
q2 = [a[1][0], a[2][1], a[3][2]]
q3 = [a[2][0], a[1][1], a[0][2]]
q4 = [a[3][1], a[2][2], a[1][3]]
if (q3.count("x") == 2 and q3.count(".") == 1) or (q4.count("x") == 2 and q4.count(".") == 1):
    t = True  
if (q1.count("x") == 2 and q1.count(".") == 1) or (q2.count("x") == 2 and q2.count(".") == 1):
    t = True
q1 = [a[0][0], a[1][1], a[2][2]]
q2 = [a[1][1], a[2][2], a[3][3]]
q3 = [a[3][0], a[2][1], a[1][2]]
q4 = [a[2][1], a[1][2], a[0][3]]
if (q3.count("x") == 2 and q3.count(".") == 1) or (q4.count("x") == 2 and q4.count(".") == 1):
    t = True  
if (q1.count("x") == 2 and q1.count(".") == 1) or (q2.count("x") == 2 and q2.count(".") == 1):
    t = True
if t:
    print("YES")
else:
    print("NO")
