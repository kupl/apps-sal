import heapq


class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        mono_inc = sorted([(i, val) for (i, val) in enumerate(A)], key=lambda x: x[1])
        mono_dec = sorted(mono_inc, reverse=True, key=lambda x: x[1])
        odd_jumps = [None] * len(mono_inc)
        for (i, el) in enumerate(mono_inc):
            j = i + 1
            while j < len(mono_inc):
                next_el = mono_inc[j]
                if next_el[0] > el[0]:
                    odd_jumps[el[0]] = next_el[0]
                    break
                j += 1
        even_jumps = [None] * len(mono_dec)
        for (i, el) in enumerate(mono_dec):
            j = i + 1
            while j < len(mono_dec):
                next_el = mono_dec[j]
                if next_el[0] > el[0]:
                    even_jumps[el[0]] = next_el[0]
                    break
                j += 1
        odd = {}
        even = {}
        i = len(A) - 1
        while i >= 0:
            if i == len(A) - 1:
                odd[i] = True
                even[i] = True
                i -= 1
                continue
            odd_dest = odd_jumps[i]
            odd[i] = even[odd_dest] if odd_dest is not None else False
            even_dest = even_jumps[i]
            even[i] = odd[even_dest] if even_dest is not None else False
            i -= 1
        return sum(odd.values())
