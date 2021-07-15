l = [0] + list(reversed(bin(int(input()))))
for i in range(len(l)-2,0,-1):
    if l[i] == '1':
        print(i,end=' ')

        

    

