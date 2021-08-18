from collections import Counter


def max_num(a, b):
    if len(b) > len(a):
        val = ''.join(sorted(a, reverse=True))
        return int(val)
    else:
        res = ''
        for i in b:
            if i in a:
                a.remove(i)
                if ''.join(b[len(res) + 1:]) >= ''.join(sorted(a)):
                    res += i
                else:
                    a.append(i)
                    break
            else:
                break
        new_b = b[len(res):]
        if new_b == []:
            return res

        for i in new_b:
            for j in range(int(i) - 1, -1, -1):
                if str(j) in a:
                    a.remove(str(j))
                    return res + str(j) + ''.join(sorted(a, reverse=True))


a = list(input())
b = list(input())
print(max_num(a, b))
