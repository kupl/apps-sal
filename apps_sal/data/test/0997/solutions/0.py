import re
try:
    while True:
        a = []
        b = []
        for word in re.split('[,;]', input()):
            (a if re.match('^(0|[1-9][0-9]*)$', word) else b).append(word)
        print('"%s"' % ','.join(a) if a else '-')
        print('"%s"' % ','.join(b) if b else '-')
except EOFError:
    pass
