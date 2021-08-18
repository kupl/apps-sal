"""
Created on Tue Sep 24 18:38:16 2019

@author: Mridul Garg
"""

L = int(input())
string = input()


q = len(string) // L
r = len(string) % L

if q == 0:
    temp = '1' + '0' * (L - 1)
    ans = temp

elif r != 0:
    temp = '1' + '0' * (L - 1)
    ans = temp * (q + 1)


else:
    temp = string[0:L]
    temp2 = temp * q
    if int(temp2) > int(string):
        ans = temp2

    else:
        if temp == '9' * L:
            temp = '1' + '0' * (L - 1)
            temp = temp * (q + 1)
            ans = temp
        else:
            temp2 = int(temp) + 1
            ans = str(temp2) * q


print(ans)
