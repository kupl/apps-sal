C = str(input())
data = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(data)):
    if C == data[i]:
        print(data[i+1])
        return
