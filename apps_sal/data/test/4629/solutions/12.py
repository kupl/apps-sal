import sys


def check(x):

    while(x != 0):
        if(x % 3 == 2):
            return False
        x = x // 3

    return True


q = int(sys.stdin.readline())

ans_arr = []

for i in range(q):
    n = int(sys.stdin.readline())

    val = n
    while(not (check(val))):
        val += 1

    ans_arr.append(str(val))

print("\n".join(ans_arr))
