t = int(input())
for i in range(t):
    s = input()
    delta = s[-2:]
    # print(delta)
    if delta == "po":
        print("FILIPINO")
    elif delta == "su":
        print("JAPANESE")
    else:
        print("KOREAN")
