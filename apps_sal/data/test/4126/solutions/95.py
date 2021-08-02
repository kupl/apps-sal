S = str(input())
N = len(S)
sList = [str(s) for s in S]
isPalindrome = 1
str1 = ''
str2 = ''
str3 = ''
str4 = ''

for i in range(N):
    if (sList[i] != sList[N - 1 - i]):
        isPalindrome = 0
if isPalindrome == 1:
    for i in range(int((N - 1) / 2)):
        str1 += sList[i]
        str2 += sList[int((N - 1) / 2 - 1 - i)]
        str3 += sList[int((N + 3) / 2 - 1 + i)]
        str4 += sList[N - 1 - i]

        if str1 != str2:
            isPalindrome = 0
        if str3 != str4:
            isPalindrome = 0
if isPalindrome == 0:
    print('No')
else:
    print('Yes')
