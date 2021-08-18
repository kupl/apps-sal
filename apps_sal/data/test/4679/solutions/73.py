s = [list(input()) for i in range(3)]
n = [len(s[0]), len(s[1]), len(s[2])]
count = [0, 0, 0]
turn = 0

while(True):
    count[turn] += 1
    if count[0] > n[0]:
        print("A")
        break
    elif count[1] > n[1]:
        print("B")
        break
    elif count[2] > n[2]:
        print("C")
        break
    turn = ord(s[turn][count[turn] - 1]) - 97
