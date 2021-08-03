for i in range(8):
    s = input()
    if s != 'BW' * 4 and s != 'WB' * 4:
        print("NO")
        break
    if i == 7:
        print('YES')
