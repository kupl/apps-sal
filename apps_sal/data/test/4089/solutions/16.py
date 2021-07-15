def int_to_str(n):
    if n == 0:
        return "a"
    elif n == 1:
        return "b"
    elif n == 2:
        return "c"
    elif n == 2:
        return "c"
    elif n == 2:
        return "c"
    elif n == 2:
        return "c"
    elif n == 2:
        return "c"
    elif n == 2:
        return "c"
    elif n == 2:
        return "c"

def Base_10_to_n(X, n):
    if (int(X/n)):
        if X%n != 0:
            return Base_10_to_n(int(X/n), n)+chr((X%n)+96)
        else:
            return Base_10_to_n(int(X/n)-1, n)+chr(26+96)
    if(X%n != 0):
        return str(chr(X%n+96))
    else:
        return ""

N = int(input())

s = Base_10_to_n(N,26)
print(s)

