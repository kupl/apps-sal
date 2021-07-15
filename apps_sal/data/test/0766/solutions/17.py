s = input()
letters = [0] * 26
if len(s) < 4:
    print('No')
else:
    for i in range(len(s)):
        letters[ord(s[i]) - 97] += 1
    kolvo = 0
    for i in range(26):
        if letters[i] > 0:
            kolvo += 1
    if kolvo > 4:
        print('No')
    elif kolvo == 3:
        print('Yes')
    elif kolvo == 1:
        print('No')
    elif kolvo == 2:
        a = 0
        b = 0
        for i in range(len(letters)):
            if letters[i] != 0 and a == 0:
                a += letters[i]
            elif letters[i] != 0 and a != 0:
                b += letters[i]
        if a != 1 and b != 1:
            print('Yes')
        else:
            print('No')
    elif kolvo == 4:
        print('Yes')
