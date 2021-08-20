class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        distinct_subs = set()
        for i in range(2, len(text) + 1, 2):
            for j in range(len(text) + 1 - i):
                sub_string = text[j:j + i]
                if sub_string[:int(i / 2)] == sub_string[int(i / 2):]:
                    if sub_string not in distinct_subs:
                        distinct_subs.add(sub_string)
        return len(distinct_subs)
