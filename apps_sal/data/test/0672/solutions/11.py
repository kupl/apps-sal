a, b = list(map(int, input().split(' ')))
diff = a - b
if a == 0 or b == 0 or diff == 0 or b > a:
    if b > a:
        print(0)
    elif a == 0 and b == 0:
        print("infinity")
    elif a == 0:
        print(0)
    elif b == 0:
        factors = []
        for i in range(1, int(diff ** 0.5) + 1):
            if diff % i == 0:
                factors.append(i)
                factors.append(int(diff / i))
        factors = list(set(factors))
        facts = [i for i in factors if i > b]
        print(len(facts))
    else:
        print("infinity")

else:
    b = b % a
    diff = a - b
    factors = []
    for i in range(1, int(diff ** 0.5) + 1):
        if diff % i == 0:
            factors.append(i)
            factors.append(int(diff / i))
    factors = list(set(factors))
    facts = [i for i in factors if i > b]
    print(len(facts))
