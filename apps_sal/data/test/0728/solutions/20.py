x = int(input(''))
rida = input('')
rida = rida.split()
nrs = list(map(int, rida))
count = nrs.pop(0)
startcount = count
while count <= max(nrs):
    ind = nrs.index(max(nrs))
    nrs[ind] = nrs[ind] - 1
    count = count + 1
print(str(count - startcount))
