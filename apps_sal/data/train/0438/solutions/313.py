class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        if len(arr) == m:
            return m

        move = -1
        l = {x: (0, 0) for x in range(len(arr) + 2)}

        for i, a in enumerate(arr):

            l[a] = (a, a)
            b, c = a, a
            # print(i,a,l)

            # Check Left
            if l[a - 1][0]:

                # Check Prev Length
                if l[a - 1][1] - l[a - 1][0] + 1 == m:
                    move = i

                # Left Boarder
                b = l[a - 1][0]

            # Check Right
            if l[a + 1][0]:
                # Check Prev Length
                if l[a + 1][1] - l[a + 1][0] + 1 == m:
                    move = i

                # Right Boarder
                c = l[a + 1][1]

            # Update
            l[a] = (b, c)
            l[b] = (b, c)
            l[c] = (b, c)

            # Check Current Length
            if l[a][1] - l[a][0] + 1 == m:
                move = i + 1

        return move
