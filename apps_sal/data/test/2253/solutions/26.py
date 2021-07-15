t = int(input())
for _ in range(0,t):
    s = input()
    if s[len(s)-2:len(s)] == "po":
        print("FILIPINO")
    elif s[len(s)-4:len(s)] == "desu" or s[len(s)-4:len(s)] == "masu":
        print("JAPANESE")
    else:
        print("KOREAN")
