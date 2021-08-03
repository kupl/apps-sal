answers = [
    "O-|-OOOO",
    "O-|O-OOO",
    "O-|OO-OO",
    "O-|OOO-O",
    "O-|OOOO-",
    "-O|-OOOO",
    "-O|O-OOO",
    "-O|OO-OO",
    "-O|OOO-O",
    "-O|OOOO-"
]

x = list(input())
x.reverse()
for i in x:
    print(answers[int(i)])
