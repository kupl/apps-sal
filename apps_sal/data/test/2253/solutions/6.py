t = int(input())
for _ in range(t):
    s = input()
    if s[-2:] == 'po':
        print("FILIPINO")
    elif s[-5:] == 'mnida':
        print("KOREAN")
    else:
        print("JAPANESE")

