import re
text = input()
alphabet = list('abcdefghijklmnopqrstuvwxyz')
output = ['-1', '-1']
for i in range(len(alphabet)):
    pattern = alphabet[i] + '.?' + alphabet[i]
    match_object = re.search('%s.?%s' % (alphabet[i], alphabet[i]), text)
    if match_object:
        output[0] = str(match_object.start() + 1)
        output[1] = str(match_object.end())
        break
print(' '.join(output))
