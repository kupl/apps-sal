def solve(word):
    banner = "CODEFORCES"

    for c in word:
        if c == banner[0]:
            banner = banner[1:]
            if len(banner) == 0:
                return True
        else:
            break

    for c in word[::-1]:
        if c == banner[-1]:
            banner = banner[:-1]
            if len(banner) == 0:
                return True
        else:
            break
    return False

import sys
word = sys.stdin.read().strip()
if solve(word) == True:
    print("YES")
else:
    print("NO")
