moji = str(input())
flg = 0
for i in range(0,3):
    if moji[i] == moji[i+1]:
        flg = 1

print(("Good","Bad")[flg == 1])
