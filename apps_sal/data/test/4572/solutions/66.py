s = input()
cnt = 0
for i in range(26):
    if chr(97 + i) in s:
        cnt += 1
        if cnt == 26:
            print("None")
            break
    else:
        print(chr(97+i))
        break
