def key(x):
    s = x.count('s')
    return s / len(x)


def sh_produce(x):
    x = str(x)
    sh = [0 for j in range(len(x))]
    if x[-1] == 'h':
        sh[-1] = 1
    for i in range(len(x) - 2, -1, -1):
        if x[i] == 'h':
            sh[i] = sh[i + 1] + 1
        else:
            sh[i] = sh[i + 1]
    sh_num = 0
    for i in range(len(x)):
        if x[i] == 's':
            sh_num += sh[i]
    return sh_num


n = int(input())
input_list = []
for i in range(n):
    tmp = input()
    input_list.append(tmp)
input_list = sorted(input_list, key=key, reverse=True)
res = ''.join(input_list)
print(sh_produce(res))
