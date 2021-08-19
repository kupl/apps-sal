string = input()
palindrome = False
palin1 = False


def palin(string):
    palindrome = False
    if string == string[::-1]:
        palindrome = True
    return palindrome


palindrome = palin(string)
if palin(string[int((len(string) - 1) / 2)]) == True and palindrome == True:
    palin1 = True
if palin(string[int((len(string) + 3) / 2) - 1:len(string)]) == True and palin1 == True:
    print('Yes')
else:
    print('No')
