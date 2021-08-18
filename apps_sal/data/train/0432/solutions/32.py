class Solution:
    def isPossibleDivide(self, A, k):
        c = collections.Counter(A)
        print(c)
        for i in sorted(c):
            print(i)
            if c[i] > 0:
                for j in range(k)[::-1]:
                    print(('j:', j, i + j, c[i + j]))
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
                print(c)
        return True
