class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        self.n = len(result)
        self.levels = []
        self.alldigit = {}
        self.allch = []
        self.result = result
        self.nonzero = set()
        for w in words:
            self.nonzero.add(w[0])
        self.nonzero.add(result[0])
 #       print(\"nonzero\", self.nonzero)
        for r in range(len(result)):
            l = []
            for w in words:
                if r < len(w):
                    l.append(w[len(w) - r - 1])

            l.append(result[len(result) - 1 - r])
            self.levels.append(l)
#        print(\"levels\", self.levels)
        self.occupy = set()
        self.checkdigit = {}  # num of words to digit

        if len(self.levels[-1]) == 1:
            self.alldigit[self.levels[-1][0]] = 1
            self.occupy.add(1)

        for l in range(len(self.levels)):
            newch = set(self.levels[l]) - set(self.allch)
            self.allch.extend(newch)
            self.checkdigit[len(self.allch)] = l + 1
#        print(\"checkdigit\", self.checkdigit)
#        print(\"allch\", self.allch)
        if self.tryone(0, len(self.allch)):
            #            print(self.alldigit)
            return True
        else:
            #            print(self.alldigit)
            return False

    def tryone(self, level, maxl):
        flag = False
        if maxl == level:
            if self.check(self.checkdigit[level]):
                #                print(\"final level\", self.alldigit)
                return True
            else:
                return False
        if level in self.checkdigit:
            if not self.check(self.checkdigit[level]):
                return False
            else:
                pass
#                if 'T' in self.alldigit and self.alldigit['T'] == 9 and level > 7:
#                    flag = True
#                    print(\"level:\", level, self.alldigit)

        if self.allch[level] in self.alldigit:
            if self.tryone(level + 1, maxl):
                return True
            else:
                return False

        for i in range(10):
            if i not in self.occupy:
                if i != 0 or self.allch[level] not in self.nonzero:
                    #                    if flag:
                    #                        print(\"level 8:\", level, i, self.allch[level])
                    self.occupy.add(i)
                    self.alldigit[self.allch[level]] = i
                    if self.tryone(level + 1, maxl):
                        return True
                    del self.alldigit[self.allch[level]]
                    self.occupy.remove(i)
        return False

    def check(self, level):
        #        flag = False
        #        if level > 5 and self.alldigit['I'] == 1 and self.alldigit['T'] >= 5:
        #            flag = True
        #            print(self.alldigit)
        #        if self.alldigit['Y'] > 1 and self.alldigit['D'] > 6 and self.alldigit['E'] > 4:
        #            flag = True
        #            print(\"check level\", level, self.alldigit)
        plus = 0
#        if level == 5 and self.alldigit['F'] == 1 and self.alldigit['U'] == 9:
#            flag = True
#            print(\"digit:\", level, self.alldigit)
        for i in range(level):
            levelsum = 0
            for j in range(len(self.levels[i]) - 1):
                levelsum += self.alldigit[self.levels[i][j]]
#            if flag:
#                print(\"level, levelsum, plus, result\", level, levelsum, plus, self.alldigit[self.levels[i][-1]])
            if (levelsum + plus) % 10 != self.alldigit[self.levels[i][-1]]:
                #                if flag:
                #                    print(\"False\")
                return False
            else:
                plus = int((levelsum + plus) / 10)
#                if flag:
#                    print(\"plus\", plus)
#        if flag:
#            print(\"True\")
        return True
