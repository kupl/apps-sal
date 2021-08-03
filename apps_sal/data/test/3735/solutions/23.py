n = input()
if len(n) == 1:
    print(int(n))
else:
    a = ""
    if n[0] != '1':
        a += chr(ord(n[0]) - 1)
    a += '9' * (len(n) - 1)
    b = str(int(n) - int(a))
    print(sum(map(int, list(a) + list(b))))
