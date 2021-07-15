'''
Using even odd approach
'''

length=int(input())
s=input()

low, high, maxlen = 0, 0, 1
for i in range(1,length):
    #even length substring palindrome check
    low = i - 1
    high = i
    while low>=0 and high<length and s[low] == s[high]:
        #while it does not overflow and palindrome property do:
        if high-low+1>maxlen:
            start, maxlen = low, high - low +1
            #start for marking longest palindromes index
            #updating maxlen as new longest palindromic strings length 
        low-=1
        high+=1
        #size increases


    #odd length substring palindrome check
    low = i-1
    high = i+1
    while low>=0 and high<length and s[low]==s[high]:
        #while it does not overflow and palindrome property do:
        if high - low +1 > maxlen:
            start, maxlen = low, high - low + 1
            #start for marking longest palindromes index
            #updating maxlen as new longest palindromic strings length
        low-=1
        high+=1
print(maxlen)
print(s[start:start+maxlen])



