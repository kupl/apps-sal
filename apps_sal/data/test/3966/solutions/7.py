inp = input()
n = int(inp)
line = input()
myarray = line.split(' ')
myarray = list(map(int, myarray))
myarray = sorted(myarray)
score = 0
if(n == 1):
    print((int(myarray[0])))
elif(n == 2):
    print(2 * (int(myarray[1]) + int(myarray[0])))
else:
    minimum = 0
    for x in range(len(myarray)):
        score = score + (x + 2) * (int(myarray[x]))
    score = score - int(int(myarray[n - 1]))
    print(score)
