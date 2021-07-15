n = int(input())
lyca = [2,1]
for i in range(2,87):
    lyca.append(lyca[i-1]+lyca[i-2])
print(lyca[n])
