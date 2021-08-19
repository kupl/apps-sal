s = input()
temp = 1 if len(s) % 2 != 0 else 2
for i in range(temp, len(s), 2):
    moji = s[:len(s) - i]
    #print(moji[:len(moji)//2], moji[len(moji)//2:])
    if moji[:len(moji) // 2] == moji[len(moji) // 2:]:
        print((len(moji)))
        break
