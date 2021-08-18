l = int(input())
tmp = [0]
stack = [1]
for i in range(l):
    line = input().split()
    if line[0] == 'add':
        tmp[-1] += 1
        if tmp[-1] >= 2 ** 32:
            print('OVERFLOW!!!')
            return
    elif line[0] == 'for':
        stack.append(int(line[1]))
        tmp.append(0)
    else:
        t = stack.pop()
        tt = tmp.pop()
        tmp[-1] += t * tt
        if tmp[-1] >= 2 ** 32:
            print('OVERFLOW!!!')
            return

print(tmp[-1])
