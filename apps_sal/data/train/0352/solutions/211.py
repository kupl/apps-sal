def isPredecessor(src, dst):
    nsrc = len(src)
    ndst = len(dst)
    if nsrc + 1 != ndst:
        return False

    i = 0
    while i < nsrc:
        if src[i] == dst[i]:
            i += 1
            continue
        else:
            return src[i:] == dst[i + 1:]

    return True


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        mem_len = [-1 for _ in range(len(words))]

        def search(i):
            if mem_len[i] != -1:
                return mem_len[i]

            ans = 1
            for j in range(i + 1, len(words)):
                if isPredecessor(words[i], words[j]):
                    mem_len[j] = search(j)
                    ans = max(ans, mem_len[j] + 1)

            mem_len[i] = ans
            return ans

        for i in range(len(words)):
            search(i)

        return max(mem_len)
