from sys import stdin, stdout

def solution():
    life = stdin.readline().strip()
    result = [[1]]

    zeros = [0]
    ones = []

    if life[0] == '1':
        print("-1")
        return

    for i in range(1, len(life)):
        if life[i] == '0':
            if ones:
                index = ones.pop()
                result[index].append(i+1)
                zeros.append(index)
            else:
                result.append([i+1])
                zeros.append(len(result) - 1)
        else:
            if zeros:
                index = zeros.pop()
                result[index].append(i+1)
                ones.append(index)
            else:
                print("-1")
                return
    #print(result)
    if ones:
        print("-1")
        return

    print(len(result))
    print('\n'.join([str(len(x))+' '+' '.join(map(str,x)) for x in result]))

solution()

