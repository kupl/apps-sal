

from itertools import product


S = input()


length = len(S)
ans = 0
for lst in product(["+", ""], repeat=length - 1):
    mystr = ""
    for i in range(length - 1):
        mystr += S[i] + lst[i]
    mystr += S[-1]
    mylist = [int(x) for x in mystr.split("+")]
    ans += sum(mylist)
print(ans)
