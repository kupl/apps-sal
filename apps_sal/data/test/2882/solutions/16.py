class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # array to keep track of results
        answers = []
        for i in range(0, n + 1):
            answers.append(Solution.catalanHelper(i, answers))
            print((i, answers))

        return list(set(answers[n]))

    @staticmethod
    # returns parenthesis
    def catalanHelper(n, answers):
        """
        : type n : int 
        : rtype : List[str]
        """

        if n == 0:
            return [""]
        elif n == 1:
            return ["()"]
        else:
            output = []
            for i in range(0, n - 1):
                front_list = answers[i]
                end_list = answers[n - i - 1]
                for front in front_list:
                    for end in end_list:

                        output.append("(" + front + ")" + end)
                        output.append("(" + front + end + ")")

            return output
