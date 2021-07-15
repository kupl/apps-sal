num = int(input())

def the_algorithm(num):
    ary = list(str(num))
    sum = 0

    for bit in range(1 << (len(ary) - 1)):
        tmp = [ary[0]]
        for i in range((len(ary) - 1)):
            mask = 1 << i

            if bit & mask:
                tmp.append(ary[i + 1])
            else:
                tmp[-1] = tmp[-1] + ary[i + 1]

        for i in tmp:
            sum += int(i)

    return sum

print(the_algorithm(num))
