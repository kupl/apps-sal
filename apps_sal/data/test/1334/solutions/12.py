n, k = list(map(int, input().split()))
s = input()
list1 = list(set(s))
list1.sort()
if(k > len(s)):
    print(s + (list1[0] * (k - len(s))))
elif(k < len(s)):
    j = k - 1
    while(j >= 0 and list1[-1] == s[j]):
        j -= 1
    st = s[0:j]
    st += (list1[list1.index(s[j]) + 1])
    st += (list1[0] * (k - j - 1))
    print(st)
else:
    j = len(s) - 1
    while(j >= 0 and list1[-1] == s[j]):
        j -= 1
    st = s[0:j]
    st += (list1[list1.index(s[j]) + 1])
    st += (list1[0] * (len(s) - j - 1))
    print(st)
