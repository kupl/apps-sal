# You lost the game.
n = int(input())
ch = str(input())
r = ""
R = ch.count("R")
B = ch.count("B")
G = ch.count("G")
if R and B and G:
    print("BGR")
elif (R >= 2 and B >= 2) or (G >= 2 and R >= 2) or (G >= 2 and B >= 2):
    print("BGR")
elif R >= 2 and (B == 1 or G == 1):
    print("BG")
elif B >= 2 and (R == 1 or G == 1):
    print("GR")
elif G >= 2 and (B == 1 or R == 1):
    print("BR")
elif B and G:
    print("R")
elif R and G:
    print("B")
elif B and R:
    print("G")
elif B:
    print("B")
elif G:
    print("G")
else:
    print("R")
