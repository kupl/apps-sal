b = [100 for i in range(8)]
w = [100 for i in range(8)]
b_temp = 0
w_temp = 0
b_min = 0
w_min = 0
field = ['' for i in range (8)]
for i in range(8):
    field[i] = input()
for i in range(8):
    for j in range(8):
        w_temp +=1
        if field[j][i] == 'B':
            w_temp = 100
        if (field[j][i] == 'W')and(w_temp < 100):
            w[i] = w_temp
            w_temp = 100
    w_temp = 0
for i in range(8):
    for j in range(8):
        b_temp += 1
        if field[7-j][i] == 'W':
            b_temp = 100
        if (field[7-j][i] == 'B')and(b_temp < 100):
            b[i] = b_temp
            b_temp = 100
    b_temp = 0        
b_min = min(b)
w_min = min(w)
if b_min < w_min:
    print('B')
else:
    print('A')




            

