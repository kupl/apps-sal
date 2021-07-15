N = int(input())

laptops = []

for i in range(N):
    string = input()
    string.strip()
    string += " "
    current = []
    current_st = ""
    for char in string:
        if char != " ":
            current_st += char
        else:
            current.append(int(current_st))
            current_st = ""
    laptops.append(current)

laptops.sort()

#print(laptops)

isReverse = False

for i in range(N-1):
    if laptops[i+1][1] < laptops[i][1]:
        isReverse = True
        print("Happy Alex")
        break

if isReverse == False:
    print("Poor Alex")

