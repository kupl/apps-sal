class Solution:

    def oddEvenJumps(self, a: List[int]) -> int:
        b = list(sorted(list(range(len(a))), key=lambda i: a[i]))
        c = list(sorted(list(range(len(a))), key=lambda i: -a[i]))
        odd_next = {}
        even_next = {}
        i = 1
        while i < len(b):
            j = i
            while j < len(b) - 1 and b[j] <= b[i - 1]:
                j += 1
            if b[j] > b[i - 1]:
                odd_next[b[i - 1]] = b[j]
            i += 1
        i = 1
        while i < len(c):
            j = i
            while j < len(c) - 1 and c[j] <= c[i - 1]:
                j += 1
            if c[j] > c[i - 1]:
                even_next[c[i - 1]] = c[j]
            i += 1
        paths = 0
        for start in list(odd_next.keys()):
            index = start
            can_go = True
            odd = True
            while can_go and index != len(a) - 1:
                if odd:
                    if index in list(odd_next.keys()):
                        index = odd_next[index]
                    else:
                        can_go = False
                elif index in list(even_next.keys()):
                    index = even_next[index]
                else:
                    can_go = False
                odd = not odd
            if index == len(a) - 1:
                paths += 1
        if len(a) - 1 not in list(odd_next.keys()):
            paths += 1
        return paths
