class A:

    def A(self, n, s):
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        s = s.upper()
        for i in alphabets:
            if i not in s:
                return 'NO'
        return 'YES'


def __starting_point():
    n = int(input())
    s = input()
    print(A().A(n, s))


__starting_point()
