class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # sort both
        #abb, aab
        s_count = dict()
        t_count = dict()
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        sim_count = 0
        for key in list(s_count.keys()):
            if t_count.get(key, 0):
                # s_count:3, t_count:1 => get t_count
                # s_count: 1, t_count: 3 => get s_count
                if s_count[key] >= t_count[key]:
                    sim_count += t_count[key]
                else:
                    sim_count += s_count[key]
        return len(s) - sim_count

        # print(sorted(s_count))
        # print(sorted(t_count))
        # print(s_count)
        # print(t_count)

        # s_sorted = sorted(s) #cannot use .sort() on str
        #t_sorted = sorted(t)
        # print(s_sorted)
        # print(t_sorted)
  #      ['c', 'd', 'e', 'l', 'o',       t']
#['a',   'c',       'e', 'i', 'p', 'r', 't']
#{'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
#{'p': 1, 'r': 1, 'a': 1, 'c': 2, 't': 1, 'i': 1, 'e': 1}

        # sim: c1, e1, t1 => 8-3 = 5
