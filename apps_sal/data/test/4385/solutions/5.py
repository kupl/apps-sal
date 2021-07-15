antennas=[]
for i in range(5):
    antennas.append(int(input('')))
limit=int(input(''))

if antennas[4]-antennas[0]>limit:
    print(":(")
else:
    print("Yay!")    

