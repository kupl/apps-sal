def re(s):
    t = ""
    for i in s:
        if(i == "2" or i == "5"):
            t += "a"
        elif(i == "6" or i == "9"):
            t += "b"
        else:
            t += i
    return t
from collections import defaultdict as dd
def main():
    t = re(input())
    s = re(input())
    req = dd(int)
    hv = dd(int)
    ans = 10**9
    for i in t:
        req[i] += 1
    for j in s:
        hv[j] += 1
    for i in t:
        ans = min(ans, hv[i] // req[i])
    print(ans)
main()
