import shlex
s = input()
a = shlex.split(s)
for x in a:
    print('<' + x + '>')
