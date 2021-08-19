
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline

n, k = map(int, input().split())

coeff = [str(input().strip()) for _ in range(n + 1)]

if coeff.count('?') == 0:
    # check game state
    total = 0
    for s in range(n + 1)[::-1]:
        total = total * k + int(coeff[s])
        if abs(total) > 1000000000000:
            break
    if total == 0:
        print("Yes")
    else:
        print("No")
elif k == 0:
    if coeff[0] == '?':
        # check if human's turn
        if (n + 1 - coeff.count('?')) % 2 == 1:
            print("Yes")
        else:
            print("No")
    else:
        if coeff[0] == '0':
            print("Yes")
        else:
            print("No")
else:
    # k is not 0
    # check if human moves last
    if (n + 1) % 2 == 0:
        print("Yes")
    else:
        print("No")
