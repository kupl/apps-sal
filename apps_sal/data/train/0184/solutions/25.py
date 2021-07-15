class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        i = 0
        diff = 1
        sol = 0
        while i < len(text):
            c = text[i]
            j = i+1
            found = False
            while j < len(text):
                if text[j] == c:
                    j+= 1
                else:
                    if found:
                        if count[c] >= j-i:
                            sol = max(sol, j-i)
                        else:
                            sol = max(sol, j-i-1)
                        break
                    found = True
                    diff = j
                    j += 1
            if j == len(text):
                if count[c] > j-i and not found:
                    sol = max(sol, j-i+1)
                if count[c] >= j-i:
                    sol = max(sol, j-i)
                else:
                    sol = max(sol, j-i-1)
                break
            i = diff
        return sol    

