class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        a, b = a % 1337, int("".join([str(i) for i in b]))
        base, temp, extra = {1: a}, 1, {a: 1}
        for temp in range(2, 1338):
            rem = base[temp - 1] * a % 1337
            if rem in extra:
                start = extra[rem]
                length = temp - start
                break
            else:
                base[temp] = rem
                extra[rem] = temp
        if b in base:
            return base[b]
        return base[start + (b - start) % length]
