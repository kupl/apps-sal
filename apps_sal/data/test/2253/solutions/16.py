t = int(input())

for t_i in range(t):
    s = input()
    if s[-2:] == "po":
        print("FILIPINO")
    elif s[-4:] in ["desu", "masu"]:
        print("JAPANESE")
    else:
        print("KOREAN")
