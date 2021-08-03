antennas = []
for i in range(5):
    antennas.append(int(input()))
k = int(input())

for e in antennas[:0:-1]:
    if e - antennas[0] > k:
        print(':(')
        break
else:
    print('Yay!')
