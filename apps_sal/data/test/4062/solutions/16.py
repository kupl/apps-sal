resultnum = []
inputnum = input().split()
for tmp in range(2):
    resultnum.append(int(inputnum[tmp]) * int(inputnum[2]))
    resultnum.append(int(inputnum[tmp]) * int(inputnum[3]))
print(str(max(resultnum)))
