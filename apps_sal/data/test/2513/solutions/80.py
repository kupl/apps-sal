n = int(input())
s = input()
s += s[0]+s[1]
case = ["SS","SW","WS","WW"]
for x in case:
    animal = x
    for i in range(1,n+1):
        if (s[i] == "o" and animal[i] == "S") or (s[i] == "x" and animal[i] == "W"):
            if animal[i-1] == "S": 
                animal += "S"
            else: 
                animal += "W"
        elif animal[i-1] == "S": 
                animal += "W"
        else: 
            animal += "S"
    if animal[-2:] == x:
        print(animal[:n])
        return
print(-1)
