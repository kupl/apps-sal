x = int(input())
cell = input()
cell2 = ''
for i in cell:
    cell2 = i + cell2 
cell3 = bin(int(cell2, 2)+1)
cell4 = cell3[2:]
cell5='0'*(x-len(cell4))
for i in cell4:
    cell5 = i + cell5 
cell6 = cell5[:x]
sa=0
for i in range(x):
    if cell6[i] != cell[i]:
        sa+=1
print(sa)

