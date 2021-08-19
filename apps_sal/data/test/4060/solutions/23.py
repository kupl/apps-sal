n = int(input())
s = input()
prefBal = [0] * n
prefBal.append(0)
prefCan = [False] * n
prefCan.append(True)
suffBal = [0] * n
suffBal.append(0)
suffCan = [False] * n
suffCan.append(True)
currBal = 0
currCan = True
for i in range(n):
    if s[i] == '(':
        prefBal[i] = currBal + 1
    else:
        prefBal[i] = currBal - 1
    currBal = prefBal[i]
    prefCan[i] = currCan and prefBal[i] >= 0
    currCan = prefCan[i]
currBal = 0
currCan = True
for i in range(n - 1, -1, -1):
    if s[i] == ')':
        suffBal[i] = currBal + 1
    else:
        suffBal[i] = currBal - 1
    currBal = suffBal[i]
    suffCan[i] = currCan and suffBal[i] >= 0
    currCan = suffCan[i]
ans = 0
for i in range(n):
    if s[i] == '(':
        if prefCan[i - 1] and suffCan[i + 1] and (prefBal[i - 1] - 1 - suffBal[i + 1] == 0):
            ans += 1
    if s[i] == ')':
        if prefCan[i - 1] and suffCan[i + 1] and (prefBal[i - 1] + 1 - suffBal[i + 1] == 0):
            ans += 1
print(ans)
