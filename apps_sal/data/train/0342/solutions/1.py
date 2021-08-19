class Solution:

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        num = 0
        record = [(-1, -1)]
        colnum = 0
        for i in board:
            rownum = 0
            cont = 0
            for j in i:
                if j == 'X':
                    if cont == 1:
                        rownum += 1
                        continue
                    else:
                        ind = 0
                        for k in record:
                            (a, b) = k
                            if (a == colnum) & (b == rownum):
                                ind = 1
                                record.append((a + 1, b))
                                record.remove((a, b))
                                break
                        if ind == 0:
                            num = num + 1
                            record.append((colnum + 1, rownum))
                            cont = 1
                if j != 'X':
                    cont = 0
                rownum += 1
            colnum += 1
        return num
