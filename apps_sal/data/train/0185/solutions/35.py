class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        arr = list(s)
        arr = [ord(el) - 48 for el in arr]

        length = 0
        n = len(s)
        curr = 0

        h = {}
        for i in range(n - 1, -1, -1):
            length += 1

            if length > k:
                length -= 1
                curr = curr >> 1

            if arr[i] == 1:
                curr = 1 << (length - 1) | curr

            if length == k:
                h[curr] = True

        return len(h) == pow(2, k)
