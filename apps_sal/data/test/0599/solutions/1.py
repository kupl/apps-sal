def palindrome(s):
    if list(s) == list(reversed(list(s))):
        return 1
    return 0

s = input()
done = 0
for i in range(0,len(s)+1):
    for j in range(97,123):
        l = s[:i]+chr(j)+s[i:]
        if palindrome(l) == 1 and done == 0:
            print(l)
            done = 1
if done == 0:
    print("NA")

