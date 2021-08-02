# "Bad"が二回出たり。"Bad""Good"になったりする。なぜだ？？　　
S = input()
Pass = list(S)

if Pass[0] == Pass[1]:
    print("Bad")
elif Pass[1] == Pass[2]:
    print("Bad")
elif Pass[2] == Pass[3]:
    print("Bad")
else:
    print("Good")
