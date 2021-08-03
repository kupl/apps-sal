s = input()
n = len(s)


def if_palindrome(s):
    x = list(s)
    y = list(s)
    y.reverse()
    if(x == y):
        return True
    return False


done = False
x = list(s)
x = list(set(x))
nn = len(x)
r = 0
for i in range(nn):
    if(s.count(x[i]) % 2 == 1):
        r += 1
    if(r > 1):
        break
if(r <= 1):
    print("First")
    done = True


if(not done):
    n = len(s)
    if(n % 2 == 1):
        print("First")
    else:
        print("Second")
