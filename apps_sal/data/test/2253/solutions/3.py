t = int(input())
while t:
    s = input()
    if s[-2] == 'p' and s[-1] == 'o':
        print("FILIPINO")
    else:
        if s[-4:] == "desu" or s[-4:] == "masu":
            print("JAPANESE")
        else:
            print("KOREAN")
    t -= 1
