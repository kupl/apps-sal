class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ln = len(text)
        if ln == 1:
            return 1
        mx = -1
        start = 0

        while start < ln:
            print(start, ',', end='')
            i = start + 1
            inx = -1
            while i < ln and (text[start] == text[i] or inx == -1):
                if text[start] != text[i]:
                    inx = i
                i += 1
            print(i, ',', end='')
            if inx != -1 and (text[start] in text[i:] or text[start] in text[:start]):
                mx = max(mx, i - start)
            elif inx == -1 and (text[start] in text[i:] or text[start] in text[:start]):
                mx = max(mx, i - start + 1)
            elif inx == -1:
                mx = max(mx, i - start)
            else:
                mx = max(mx, i - start - 1)
            if inx == -1:
                start = i
            else:
                start = inx
            print(mx)

        return mx
