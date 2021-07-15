def ba(s):
    c1 = s.find('[')
    c2 = s.find(':', c1+1)
    c3 = s.rfind(']', c2+1)
    c4 = s.rfind(':', c2+1, c3)
    if -1 in [c1, c2, c3, c4]:
        return -1
    return s.count('|', c2, c4)+4


print(ba(input()))


