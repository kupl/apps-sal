
import time


def polytest(str):
    flag = True
    for i in range(divmod(len(str), 2)[0]):
        if str[i] != str[-i - 1]:
            flag = False
            break
    return flag


str = input()
k = int(input())

start = time.time()
dm = divmod(len(str), k)

if dm[1] != 0:
    ans = "NO"
else:
    for i in range(k):
        ans = "YES"
        if polytest(str[i * dm[0]: (i + 1) * dm[0]]) == False:
            ans = "NO"
            break

print(ans)
finish = time.time()
