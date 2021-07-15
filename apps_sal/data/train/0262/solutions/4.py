class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max([len(w) for w in words]) > len(result):
            return False
        lead_letters = set([w[0] for w in words + [result]])

        letters = []
        for k in range(1, len(result) + 1):
            for w in words:
                if len(w) >= k and w[-k] not in [x[0] for x in letters]:
                    letters.append((w[-k], k))
            letters.append((result[-k], -k))

        # print(letters)

        letter2num = {}
        num2letter = ['']*10
        nums = '0123456789'

        def helper(k):
            if k == len(letters):
                return True
            letter, digit = letters[k][0], letters[k][1]
            if digit < 0:
                left = sum([int(''.join([letter2num[ch] for ch in w[digit:]])) for w in words])
                if left < 10 ** (-digit-1):
                    return False
                num = int(str(left)[digit])
                if letter not in letter2num and not num2letter[num]:
                    letter2num[letter] = str(num)
                    num2letter[num] = letter
                    if helper(k + 1):
                        return True
                    letter2num.pop(letter)
                    num2letter[int(num)] = ''
                elif num2letter[num] != letter or (letter in letter2num and letter2num[letter] != str(num)):
                    return False
                else:
                    return helper(k + 1)

            else:
                if letter not in letter2num:
                    num_range = nums if letter not in lead_letters else nums[1:]
                    for num in num_range:
                        if not num2letter[int(num)]:
                            letter2num[letter] = num
                            num2letter[int(num)] = letter
                            if helper(k+1):
                                return True
                            letter2num.pop(letter)
                            num2letter[int(num)] = ''
                    return False
                else:
                    return helper(k + 1)

        return helper(0)
