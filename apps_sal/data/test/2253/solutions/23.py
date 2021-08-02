n = int(input())
for _ in range(n):
    s = input()
    if s.endswith("po"):
        print("FILIPINO")
    elif s.endswith("mnida"):
        print("KOREAN")
    else:
        print("JAPANESE")
