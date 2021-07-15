
def check(string, arr):
    tmp = []
    for i in range(1, len(string)):
        tmp.append(string[:i])
        tmp.append(string[i:])
    tmp = sorted(tmp)
    narr = sorted(arr)
    return tmp == narr

size = int(input())
values = []
tokens = []

for _ in range(2 * size - 2):
    values.append(input())

for value in values:
    if len(value) == size - 1:
        tokens.append(value)

if check(tokens[0] + tokens[1][-1], values):
    origin = tokens[0] + tokens[1][-1]
else:
    origin = tokens[1] + tokens[0][-1]

answer = ''
was = set()

for value in values:
    if origin.startswith(value) and not value in was:
        answer += 'P'
    else:
        answer += 'S'
    was.add(value)

print(answer)

