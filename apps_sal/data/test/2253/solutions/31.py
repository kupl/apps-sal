n = int(input())

for i in range(0, n):
    st = list(input())
    if "".join(st[-2:]) == "po":
        print("FILIPINO")
    elif "".join(st[-4:]) == "masu" or "".join(st[-4:]) == "desu":
        print("JAPANESE")
    elif "".join(st[-5:]) == "mnida":
        print("KOREAN")
