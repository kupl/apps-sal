n = hex(int(input()))[2:].upper()
q = n.count('0') * 1
q += n.count('4') * 1
q += n.count('6') * 1
q += n.count('8') * 2
q += n.count('9') * 1
q += n.count('A') * 1
q += n.count('B') * 2
q += n.count('D') * 1
print(q)
