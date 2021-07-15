for i in range(5):
    inp = input().split(' ')
    if  "1" in inp:
        print(abs(2-i)+abs(2-inp.index("1")))
        break

