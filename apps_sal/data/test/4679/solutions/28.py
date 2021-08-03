d = {'a': input(), 'b': input(), 'c': input()}
pointer = 'a'
while True:
    if 0 < len(d[pointer]):
        tmp = d[pointer][0]
        d[pointer] = d[pointer][1:]
        pointer = tmp
    else:
        print((pointer.upper()))
        break
