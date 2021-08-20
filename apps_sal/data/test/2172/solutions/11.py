first_line = list(map(int, input().split(' ')))
length_speech = first_line[0]
dictionary_len = first_line[1]
dict = {}
for i in range(dictionary_len):
    line = list(input().split(' '))
    dict[line[0]] = line[1]
speech = list(input().split(' '))
for i in range(len(speech)):
    w = speech[i]
    if len(dict[w]) < len(w):
        speech[i] = dict[w]
print(' '.join(speech))
