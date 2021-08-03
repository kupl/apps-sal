t = int(input())
for i in range(t):
    s = input()
    if s[-2:] == "po":
        print("FILIPINO")
    elif s[-4:] == "masu" or s[-4:] == "desu":
        print("JAPANESE")
    elif s[-5:] == "mnida":
        print("KOREAN")
