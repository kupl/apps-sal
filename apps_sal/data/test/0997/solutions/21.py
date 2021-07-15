s = input()
a = []
b = []
last_word = []
temp = 0
digits = "0123456789"
for letter in s:
    if letter == ";" or letter == ",":
        for leter in last_word:
            if digits.find(leter) == -1:
                temp = 1
                break
        if temp == 0 and len(last_word) != 0:
            if last_word[0] != "0" or len(last_word) == 1:
                a += ("".join(last_word)).split()
            else:
                b += ("".join(last_word)).split()
        elif len(last_word) == 0:
            temp = 0
            b += [""]
        else:
            temp = 0
            b += ("".join(last_word)).split()
        last_word = []
    else:
        last_word += letter
for leter in last_word:
        if digits.find(leter) == -1:
            temp = 1
            break
if temp == 0 and len(last_word) != 0:
    if last_word[0] != "0" or len(last_word) == 1:
        a += ("".join(last_word)).split()
    else:
        b += ("".join(last_word)).split()
elif len(last_word) == 0:
    temp = 0
    b += [""]
else:
    temp = 0
    b += ("".join(last_word)).split()
    
if len(a) == 0:
    print("-")
else:
    print('"',end="")
    print(",".join(a),end="")
    print('"')
    
if len(b) == 0:
    print("-")
else:
    print('"',end="")
    print(",".join(b),end="")
    print('"')

