s = str(input())
fans = 1
first = s[0]
last = s[-1]
i = 0
j = len(s) - 1
tempans = 1
turns = 0
counter = len(s) - 1
while i < counter and i < j and (i < len(s) - 1):
    if turns % 2 == 0:
        if s[i] != s[i + 1]:
            tempans += 1
            fans = max(tempans, fans)
            i += 1
        elif first == last:
            tempans = 1
            i += 1
        else:
            first = s[i]
            last = s[i + 1]
            tempans += 1
            fans = max(tempans, fans)
            i += 1
            turns += 1
            j = counter
    elif s[j] != s[j - 1]:
        tempans += 1
        fans = max(tempans, fans)
        j -= 1
        counter -= 1
    elif first == last:
        tempans = 1
        j -= 1
        counter -= 1
    else:
        first = s[j]
        last = s[j - 1]
        tempans += 1
        fans = max(tempans, fans)
        j -= 1
        turns += 1
        counter = j
i = len(s) - 1
j = 0
counter = 0
first = s[0]
last = s[-1]
turns = 0
tempans = 1
while i > counter and i > j and (i > 0):
    if turns % 2 == 0:
        if s[i] != s[i - 1]:
            tempans += 1
            fans = max(fans, tempans)
            i -= 1
        elif first == last:
            tempans = 1
            i -= 1
        else:
            first = s[i - 1]
            last = s[i]
            tempans += 1
            fans = max(fans, tempans)
            i -= 1
            turns += 1
            j = counter
    elif s[j] != s[j + 1]:
        tempans += 1
        fans = max(tempans, fans)
        j += 1
        counter += 1
    elif first == last:
        tempans = 1
        j += 1
        counter += 1
    else:
        first = s[j]
        last = s[j + 1]
        tempans += 1
        fans = max(tempans, fans)
        j += 1
        turns += 1
        counter = j
print(fans)
