t=0
inputa=int(input())

string=""
for x in range(inputa):
    add=input()
    string+=add
stringlen=len(string)
for char in range(stringlen-1):
    if string[char]==string[char+1]:
        t=t+1
print(t+1)
