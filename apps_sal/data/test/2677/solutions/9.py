# cook your dish here
try:
    s = input()
    v = ['A', 'E', 'I', 'O', 'U']
    consec = False
    constants = []
    cons_count = 0
    for i in range(len(s)):
        if s[i] not in constants and s[i] not in v:
            constants.append(s[i])
            cons_count += 1
    for i in range(len(s) - 2):
        if s[i] in v and s[i + 1] in v and s[i + 2] in v:
            consec = True
            break
    if cons_count >= 5 and consec == True:
        print('GOOD')
    else:
        print(-1)

except:
    pass
