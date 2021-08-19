class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        ans = set()
        lens = n
        for l in range(1, lens + 1):
            for i in range(lens - l + 1):
                j = i + l - 1
                # print(i,j)
                curr1 = text[i:j + 1]
                # print(curr1)
                curr2 = ''
                if(j + l + 1 <= n):
                    curr2 = text[j + 1:j + 1 + l]
                if(curr1 == curr2):
                    ans.add(curr1 + curr2)
        return len(ans)
