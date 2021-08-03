from collections import Counter


def max_num(a, b):
    if len(b) > len(a):
        val = ''.join(sorted(a, reverse=True))
        return int(val)
    else:
        # int_a=int(''.join(sorted(a)))
        # int_b=int(''.join(b))
        # for i in range(int_b,int_a-1,-1):
        #     # print(str(i),str(int_a))
        #     if Counter(str(i)) == Counter(str(''.join(a))):
        #         return i
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
        # print(res)
        # return res
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
