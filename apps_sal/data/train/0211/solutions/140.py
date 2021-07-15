class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def all_partitions(string):
            for cutpoints in range(1 << (len(string)-1)):
                result = []
                lastcut = 0
                for i in range(len(string)-1):
                    if (1<<i) & cutpoints != 0:
                        result.append(string[lastcut:(i+1)])
                        lastcut = i+1
                result.append(string[lastcut:])
                yield result
        # d = {}
        ps = all_partitions(s)
        
        # for p in ps:
        #     print(p)
        ret = 0
        for p in ps:
            l = list(dict.fromkeys(p))
            if (len(p) == len(l)):
                ret = max(ret, len(p))
                # print(\"OK\")
                # print(p)
                # print(l)
                # print()
            #else:
                # print(\"NG\")
                # print(p)
                # print(l)
                # print()
        return ret
#         sps = []
#         for p in ps:
#             sps.append(sorted(p))
#         for p in sps:
#             print(p)
#         for p in ps:
#             d[p.sort()] = 0
#         for p in ps:
#             d[p.sort()] += 1
        
#         ret = 0
#         for p in ps:
#             if d[p.sort()] == 1:
#                 ret += 1
#         return ret

