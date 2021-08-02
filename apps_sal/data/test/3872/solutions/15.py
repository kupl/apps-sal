a = input()
b = input()
mas = {}


def rasch(a, b):
    nonlocal mas
    s = a + b
    if a == b:
        mas[s] = 2
        return True
    else:

        if mas.get(s): return True if mas[s] == 2 else False
        if len(a) % 2 == 0:
            a1 = a[0:len(a) // 2]
            a2 = a[len(a) // 2:]
            b1 = b[0:len(a) // 2]
            b2 = b[len(a) // 2:]
            res = (rasch(a1, b1) and rasch(a2, b2)) or (rasch(a1, b2) and rasch(a2, b1))
            mas[s] = (2 if res else 1)
            return res
        else: return False


print("YES") if rasch(a, b) else print("NO")
