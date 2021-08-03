class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:

        if len(s) != len(t):
            return False

        rotations, extra = divmod(k, 26)

        diff = []

        for index in range(len(s)):
            difference = ord(t[index]) - ord(s[index])
            if difference:
                diff.append(difference)

        dictionary = dict()

        for number in range(1, 26):
            dictionary[number] = rotations

            if number <= extra:
                dictionary[number] += 1

        if not diff:
            return True

        for d in diff:

            if d < 0:
                net_d = d + 26
                if dictionary[net_d]:
                    dictionary[net_d] -= 1

                else:
                    return False

            else:
                if dictionary[d]:
                    dictionary[d] -= 1

                else:
                    return False

        return True
