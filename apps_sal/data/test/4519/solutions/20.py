def __starting_point():

    q = int(input())

    for t in range(q):
        n, k = [int(i) for i in input().split(" ")]
        s = list(input())

        zero = []
        for i in range(len(s)):
            if s[i] == '0':
                zero.append(i)

        var = 0
        index = 0

        while k > 0 and var < len(zero) and index < len(s):
            temp = zero[var]
            if k < zero[var]-index:
                s[zero[var]-k], s[zero[var]] = s[zero[var]], s[zero[var]-k]
                k = 0
            else:
                s[index], s[zero[var]] = s[zero[var]], s[index]
                k -= zero[var]-index
            var += 1
            index += 1

        print("".join(s))




__starting_point()
