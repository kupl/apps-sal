class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        bins = {}
        numbers = {}
        st = s
        print(k)

        def bin2dec(a):
            val = 0
            for i in range(len(a)):
                if a[i] == '1':
                    val += pow(2, len(a) - 1 - i)
            return val
        for i in range(len(st) - k + 1):
            if st[i:i + k] in bins:
                continue
            else:
                bins[st[i:i + k]] = 1
        for i in bins:
            numbers[bin2dec(i)] = 1
        c = 0
        for i in range(pow(2, k)):
            if i in numbers:
                c += 1
        print((c, k))
        if c == pow(2, k):
            return True
        else:
            return False
