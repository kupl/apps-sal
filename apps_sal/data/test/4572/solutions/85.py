s = input()
alpabet = [chr(x) for x in range(97,123)]
try:
    for a in alpabet:
        s.index(a)
    else:
        print(None)
except ValueError as e:
    print(a)
