class Solution:

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        variants = [n]
        nsteps = 0
        seen = set()
        while True:
            n = len(variants)
            for i in range(n):
                v = variants[i]
                if v == 1:
                    return nsteps
                if v % 2 == 0:
                    x = v // 2
                    if x in seen:
                        variants[i] = 0
                    else:
                        variants[i] = x
                        seen.add(x)
                else:
                    for x in (v - 1, v + 1):
                        if x not in seen:
                            variants.append(x)
                            seen.add(x)
            nsteps += 1
