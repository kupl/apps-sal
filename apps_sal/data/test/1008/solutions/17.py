from sys import*
def pol(s):
    n = len(s)
    for i in range(n // 2 + 1):
        if s[i] != s[-1 - i]:
            return False
    return True
s = input()
k = int(input())
if len(s) % k == 0:
    n = len(s) // k
    for i in range(k):
        #print(s[0 : n])
        if not pol(s[0 : n]):
            print("NO")
            return
        s = s[n:]
    print("YES")
            
else:
    print("NO")

