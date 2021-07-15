n = input()
for i in range(int(n)):
    s = input()
    if(s[-2:]=="po"):
        print("FILIPINO")
    elif(s[-4:]=="desu" or s[-4:]=="masu"):
        print("JAPANESE")
    else:
        print("KOREAN")

