class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def all_partitions(string):
            for cutpoints in range(1 << (len(string) - 1)):
                result = []
                lastcut = 0
                for i in range(len(string) - 1):
                    if (1 << i) & cutpoints != 0:
                        result.append(string[lastcut:(i + 1)])
                        lastcut = i + 1
                result.append(string[lastcut:])
                yield result
        ps = all_partitions(s)

        ret = 0
        for p in ps:
            l = list(dict.fromkeys(p))
            if (len(p) == len(l)):
                ret = max(ret, len(p))
        return ret
