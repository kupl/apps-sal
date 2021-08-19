def main(s):
    type = 0
    temp = ''
    answer = []
    for c in s:
        if type == 0:
            if c == ' ':
                if temp != '':
                    answer.append(temp)
                    temp = ''
            elif c == '"':
                if temp != '':
                    answer.append(temp)
                    temp = ''
                type = 1
            else:
                temp += c
        elif type == 1:
            if c == '"':
                type = 0
                answer.append(temp)
                temp = ''
            else:
                temp += c
    if type == 0 and temp != '':
        answer.append(temp)
    q = ''
    for item in answer:
        q += '<' + item + '>\n'
    return q[:-1]


def init():
    s = input()
    print(main(s))


init()
