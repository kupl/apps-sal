# class Solution:
#     def distinctEchoSubstrings(self, text: str) -> int:
#         ans = set()

#         for i in range(len(text)-1):
#             for j in range(i+1, (i+len(text))//2+1):
#                 if text[i:j] == text[j:2*j-i]: ans.add(text[i:j])

#         return len(ans)
from collections import defaultdict, deque


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        if all(x == text[0] for x in text):
            # handle worst case seperately
            return len(text) // 2

        res = set()
        character_locations = defaultdict(lambda: deque())
        for i, c in enumerate(text):
            for j in character_locations[c]:
                if i + (i - j) > len(text):
                    break

                # Use startswith to improve result slightly
                if text.startswith(text[i:i + i - j], j):
                    res.add(text[j:i + i - j])

            character_locations[c].appendleft(i)

        return len(res)
