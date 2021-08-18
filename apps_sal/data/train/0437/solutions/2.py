'''
this problem is recursive
Split the string S into (encoded substring, number, unencoded string)
If K is in the unencoded part, then we can just return the correct value
If K is in the encoded part, we recurse

I either need the length of the unencoded string, or try the encoded part first and
return (None, length) if it isn't there

'''


class Solution:
    def _decode(self, s, k):
        number_ix = -1
        for i in reversed(range(len(s))):
            if s[i].isnumeric():
                number_ix = i
                break

        if number_ix == -1:
            if k < len(s):
                return (s[k], None)
            else:
                return (None, len(s))
        else:
            encoded, number, unencoded = s[:number_ix], s[number_ix], s[number_ix + 1:]
            sub_answer, sub_length = self._decode(encoded, k)
            if sub_answer is not None:
                return (sub_answer, None)
            else:
                if k < sub_length * int(number):
                    k = k % sub_length
                    sub_answer, _ = self._decode(encoded, k)
                    return (sub_answer, None)

                k = k - (sub_length * int(number))
                if k < len(unencoded):
                    return (unencoded[k], None)
                else:
                    return (None, sub_length * int(number) + len(unencoded))

    def decodeAtIndex(self, S: str, K: int) -> str:
        answer, _ = self._decode(S, K - 1)
        return answer
