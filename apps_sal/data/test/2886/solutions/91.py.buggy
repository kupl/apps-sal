import re
text = input()
for i in list('abcdefghijklmnopqrstuvwxyz'):
    match_object = re.search(r'{0}.?{0}'.format(i), text)
    if match_object:
        print(str(match_object.start() + 1) + ' ' + str(match_object.end()))
        return
print('-1 -1')
