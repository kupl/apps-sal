n=int(input())
def good(ar):
    return ar.count("1")!=ar.count("0")
s=input()
if(good(s)):
    print(1)
    print(s)
else:
    print(2)
    print(s[0],s[1:])

