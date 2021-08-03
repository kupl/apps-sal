class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """

        n = bin(num)[2:]
        mem = [-1] * (len(n) + 1)
        mem[0] = 0
        mem[1] = 0

        def cons(n):

            count = 0
            if n == '' or n == '1':
                return 0

            if n[0] == '0':
                count += cons(n[1:])
            else:
                if (mem[len(n[1:])] == -1):
                    mem[len(n[1:])] = cons('1' * len(n[1:]))

                count += mem[len(n[1:])]

                if n[1] == '1':
                    count += 1
                    if(n[2:] != ''):
                        count += int(n[2:], 2)
                    count += mem[len(n[2:])]
                else:
                    count += cons(n[2:])

            return count

        c = cons(n)

        return num + 1 - c
