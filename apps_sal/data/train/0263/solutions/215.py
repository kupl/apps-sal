class Solution:
    main_dic = {}

    def __init__(self):
        dic = {}
        for i in range(4):
            for j in range(3):
                if i == 3 and (j == 0 or j == 2):
                    continue
                dic[i, j] = self.get_ind(i, j)
        self.main_dic = dic

    def get_ind(self, i, j):
        lst = []
        lst.append((i + 2, j - 1))
        if not self.check_ind(lst[-1]):
            lst.pop()
        lst.append((i + 2, j + 1))
        if not self.check_ind(lst[-1]):
            lst.pop()
        lst.append((i - 2, j - 1))
        if not self.check_ind(lst[-1]):
            lst.pop()
        lst.append((i - 2, j + 1))
        if not self.check_ind(lst[-1]):
            lst.pop()
        lst.append((i + 1, j + 2))
        if not self.check_ind(lst[-1]):
            lst.pop()
        lst.append((i - 1, j + 2))
        if not self.check_ind(lst[-1]):
            lst.pop()
        lst.append((i + 1, j - 2))
        if not self.check_ind(lst[-1]):
            lst.pop()
        lst.append((i - 1, j - 2))
        if not self.check_ind(lst[-1]):
            lst.pop()
        return lst

    def check_ind(self, t):
        (i, j) = t
        if i < 0 or j < 0:
            return False
        if i > 3 or j > 2:
            return False
        if i == 3 and (j == 0 or j == 2):
            return False
        return True

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        old = [[1] * 3 for i in range(4)]
        (old[3][0], old[3][2]) = (0, 0)
        for k in range(n - 1):
            new = []
            for i in range(4):
                temp = []
                for j in range(3):
                    if i == 3 and (j == 0 or j == 2):
                        temp.append(0)
                        continue
                    (lst, res) = (self.main_dic[i, j], 0)
                    for (m, n) in lst:
                        res += old[m][n]
                    temp.append(res)
                new.append(temp)
            old = new
        res = sum([sum(l) for l in old])
        return res % (10 ** 9 + 7)
