mode = input()
message = input()
keyboard = ["qwertyuiop", 
"asdfghjkl;",
"zxcvbnm,./"]
if mode=="R":
    char = dict()
    for i in range(3):
        for j in range(1, len(keyboard[i])):
            char[keyboard[i][j]] = keyboard[i][j-1]
    for i in range(len(message)):
        print(char[message[i]], end='')
else:
    char = dict()
    for i in range(3):
        for j in range(len(keyboard[i])-1):
            char[keyboard[i][j]] = keyboard[i][j+1]
    for i in range(len(message)):
        print(char[message[i]], end='')    
