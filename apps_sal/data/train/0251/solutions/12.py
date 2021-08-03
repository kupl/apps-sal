class Solution:
    def clumsy(self, n):

        def helper(arr):

            s = arr[0][0]

            for i in range(1, len(arr)):

                if i % 2 != 0:

                    s += arr[i][0]

                else:

                    s -= arr[i][0]

            return s

        if n < 2:

            return 1

        arr = [[n]]

        n -= 1

        x = 1

        while n != 0:

            if x == 5:

                x = 1

            if x == 1:

                arr[len(arr) - 1][0] *= n

            if x == 2:

                arr[len(arr) - 1][0] = int(arr[len(arr) - 1][0] / n)

            if x == 3 or x == 4:

                arr.append([n])

            n -= 1
            x += 1

        return helper(arr)
