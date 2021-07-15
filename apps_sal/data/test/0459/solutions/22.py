moves = [
    [1,3,5,7,9,11,24,22],
    [2,4,6,8,10,12,23,21],
    [13,14,5,6,17,18,21,22],
    [15,16,7,8,19,20,23,24],
    [2,1,13,15,11,12,20,18],
    [4,3,14,16,9,10,19,17]
    ]
data = [0]+list(map(int, input().split()))

def check(data):
    if data[1]==data[2]==data[3]==data[4] and data[5]==data[6]==data[7]==data[8] and data[9]==data[10]==data[11]==data[12] and data[13]==data[14]==data[15]==data[16] and data[17]==data[18]==data[19]==data[20] and data[21]==data[22]==data[23]==data[24]:
        return True
    else:
        return False

for row in moves:
    temp = data[:]
    for i in range(8):
        temp[row[i]]=data[row[(i+2)%8]]
    if check(temp):
        print('YES')
        break
    temp = data[:]
    for i in range(8):
        temp[row[i]]=data[row[(8+i-2)%8]]
    if check(temp):
        print('YES')
        break
else:
    print('NO')

