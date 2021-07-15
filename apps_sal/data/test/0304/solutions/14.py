def main():
    ast = []
    def fact(x):
        if x == 0:
            return 1
        return x * fact(x - 1)
    n = input()
    def helper(dc):
        a = 0
        temp = [dc[j] for j in dc if j != '0']
        s = sum(temp)
        try:
            ret = fact(s) * fact(s + dc['0'] - 1) // (fact(s - 1) * fact(dc['0']))
        except:
            ret = fact(s)
        for i in temp:
            ret = ret // fact(i)
        for i in dc:
            if dc[i] != 1:
                d = {}
                for j in dc:
                    d[j] = dc[j]
                d[i] -= 1
                if str(d) not in ast:
                    ast.append(str(d))
                    a += helper(d)
        return ret + a
    dct = {}
    for i in set(n):
        dct[i] = n.count(i)
    print(helper(dct))
    return 0
main()

